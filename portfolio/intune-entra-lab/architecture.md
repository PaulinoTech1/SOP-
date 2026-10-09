# Architecture: Intune / Entra ID security lab

Contoso-style test tenant for a fictional auto dealership ("Sonia's Auto Sales"). No real users or data. Group names below are the lab's real naming convention; all identifiers (tenant, object IDs, accounts) are omitted.

```mermaid
flowchart LR
    %% ---------- Identities ----------
    subgraph ID["Identities"]
        ADM["Lab admin<br/>(daily Global Admin)"]
        PIL["20 pilot users<br/>(cloud-only)"]
        BG["2 break-glass<br/>Global Admins<br/>(cloud-only, unlicensed)"]
    end

    %% ---------- Groups ----------
    subgraph GRP["Security groups"]
        MU["SG-All-Managed-Users"]
        BGX["SG-BreakGlass-CA-Exclude"]
        NP["SG-Dealership-Engineers<br/>SG-Business-Users"]
        subgraph RAG["Role-assignable groups (P1)"]
            ITA["SG-Dealership-IT-Admins"]
            SDS["SG-Service-Desk-Support"]
            SEC["SG-Security-Compliance"]
        end
    end

    PIL --> MU
    BG --> BGX

    %% ---------- Licensing ----------
    subgraph LIC["Licensing (stacked trials, 25 seats each)"]
        P1["Entra ID P1"]
        IP1["Intune Plan 1"]
    end
    MU -- "group-based licensing" --> P1
    MU -- "group-based licensing" --> IP1
    ADM -- "direct" --> P1
    ADM -- "direct" --> IP1

    %% ---------- Directory roles ----------
    subgraph ROLES["7 standing least-privilege directory roles"]
        R1["Application Admin<br/>User Admin<br/>Groups Admin<br/>Intune Admin"]
        R2["Helpdesk Admin"]
        R3["Security Reader<br/>Compliance Admin"]
        HOLD["Held for PIM (P2):<br/>Privileged Auth Admin<br/>Security Admin"]
    end
    ITA --> R1
    SDS --> R2
    SEC --> R3
    SDS -. "deferred" .-> HOLD
    SEC -. "deferred" .-> HOLD

    %% ---------- Conditional Access ----------
    subgraph CA["Conditional Access (Security Defaults OFF)"]
        CAP["CA-Require-MFA-TOTP-or-FIDO<br/>All users / all cloud apps<br/>state: enabled"]
        AS["Custom auth strength:<br/>Authenticator push or TOTP,<br/>FIDO2, Windows Hello<br/>(SMS + voice disabled)"]
    end
    CAP --> AS
    BGX -. "excluded" .-> CAP
    MU --> CAP

    %% ---------- Intune ----------
    subgraph INT["Intune (assigned to SG-All-Managed-Users)"]
        CMP["Compliance: require BitLocker"]
        BLK["Config: BitLocker XTS-AES256,<br/>silent, keys escrowed to Entra first"]
        ESP["Enrollment Status Page"]
        WU["WUfB ring: quality 7d/7d,<br/>feature 14d/7d, 2d grace"]
        SCOPE["MDM user scope = this group"]
        AP["Autopilot profile:<br/>BLOCKED (backend 400,<br/>under investigation)"]
    end
    MU --> CMP
    MU --> BLK
    MU --> ESP
    MU --> WU
    MU --> SCOPE
    MU -. "pending" .-> AP

    classDef blocked fill:#fde2e2,stroke:#c0392b,color:#000;
    classDef held fill:#fff4d6,stroke:#b9770e,color:#000;
    classDef bg fill:#e8f0fe,stroke:#1a5276,color:#000;
    class AP blocked;
    class HOLD held;
    class BG,BGX bg;
```

## Reading the diagram

- **Solid arrows** are live, verified configuration. **Dotted arrows** are exclusions, deferrals, or blocked work.
- **One group drives the endpoint baseline.** SG-All-Managed-Users is the target for licensing, Conditional Access scope, every Intune policy, and the MDM user scope. Adding a user to it is the whole onboarding step.
- **Break-glass is outside everything.** Two cloud-only Global Admins sit in an exclusion group that the CA policy skips, and they hold no licenses.
- **Admin access goes through groups, not people.** Roles are assigned to role-assignable groups. The two most sensitive roles are held back until PIM (Entra ID P2) can make them just-in-time.
- **Autopilot is the open item.** The deployment profile cannot be created yet (see the case study).

Rendered image: [`architecture.png`](architecture.png)
