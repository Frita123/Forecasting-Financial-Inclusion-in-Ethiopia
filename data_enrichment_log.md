# Data Enrichment Log – Task 1

This document records all manual and derived enrichments applied to the
Ethiopia Financial Inclusion dataset in Task 1. The purpose is to ensure
transparency, reproducibility, and traceability between enrichment,
exploratory analysis (Task 2), and future impact modeling.

---

## 1. Objectives of Enrichment

The original dataset had limited coverage of:
- Post-2021 mobile money developments
- Major market and policy events
- Explicit causal hypotheses linking events to outcomes

Enrichment was performed to:
- Capture key drivers of **Usage** and **Access**
- Enable temporal analysis in EDA
- Provide structured inputs for impact modeling

---

## 2. Added Observations

| Record ID | Indicator Code | Description | Pillar | Source | Rationale |
|---------|---------------|-------------|--------|--------|-----------|
| REC_NEW_001 | TELEBIRR_USERS | Telebirr active users (54M) | USAGE | Ethio Telecom | Captures dominant mobile money platform growth |
| REC_NEW_002 | SMARTPHONE_PEN | Smartphone penetration (%) | USAGE | GSMA | Upper bound for app-based financial usage |
| REC_NEW_003 | MPESA_USERS | M-Pesa active users (10M) | USAGE | Safaricom | Measures competitive entry and adoption |

---

## 3. Added Events

| Record ID | Event | Date | Category | Rationale |
|---------|------|------|----------|-----------|
| EVT_NEW_001 | Telebirr Launch | 2021-05 | Product launch | Major shift in digital payments landscape |
| EVT_NEW_002 | M-Pesa Launch | 2023-03 | Product launch | Market competition and new usage channel |
| EVT_NEW_003 | EthSwitch Interoperability | 2022-08 | Infrastructure | Enables cross-platform payments |
| EVT_NEW_004 | Fayda Digital ID Rollout | 2023-01 | Policy | Reduces KYC barriers for Access |

---

## 4. Added Impact Links (Hypotheses)

| Link ID | From | To | Pillar | Lag (Months) | Hypothesis |
|-------|------|----|--------|-------------|------------|
| LNK_NEW_001 | Telebirr Launch | DIGITAL_PAYMENTS | USAGE | 6 | Mobile wallets increase transaction usage |
| LNK_NEW_002 | EthSwitch | DIGITAL_PAYMENTS | USAGE | 3 | Interoperability accelerates usage |
| LNK_NEW_003 | Fayda ID | ACCOUNT_OWNERSHIP | ACCESS | 6 | Digital ID improves onboarding |

> Note: Impact links represent **hypothesized causal relationships**, not
confirmed causality. They are intended for testing in later modeling phases.

---

## 5. Link to Task 2 (EDA)

- Enriched usage indicators explain why **usage grows faster than ownership**
- Event overlays confirm that Telebirr drove usage, not Access
- Infrastructure indicators help explain the **registered vs active gap**

---

## 6. Link to Future Modeling (Task 3)

These enrichments enable:
- Event-study designs
- Lagged impact modeling
- Hypothesis testing of Access vs Usage drivers
