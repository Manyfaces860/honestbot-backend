# AuraGear Internal Knowledge Base
## RAG Customer Support Agent — Source Documents
> **NOTICE:** This knowledge base is for internal use only. Documents marked `Confidential` must never be surfaced to customers.

---

# DOCUMENT 1

```
Document ID:     AG-1001
Department:      Customer Experience / Returns
Last Updated:    2026-01-15
Confidentiality: Public
Version:         4.2
```

## General Refund & Return Policy (v4.2)

### Overview

AuraGear is committed to customer satisfaction. This policy governs all product returns and refund requests across our direct sales channels (auragear.com, AuraGear App, and AuraGear retail stores). Third-party marketplace purchases (e.g., Amazon, Flipkart) are subject to those platforms' own return policies and are outside the scope of this document.

---

### 1. Standard Return Window

Customers may return most items within **30 calendar days** of the confirmed delivery date. The product must be:

- In its original packaging (box, inserts, accessories)
- Undamaged and free from physical alterations
- Accompanied by the original proof of purchase (order confirmation email or receipt)

Refunds are processed to the original payment method within **5–7 business days** after the returned item is received and inspected at our fulfillment center.

---

### 2. Restocking Fees

Under the standard policy, **no restocking fee** is charged for items returned in original, unopened condition. A restocking fee of **10%** applies to opened items that are otherwise eligible for return (e.g., item was opened but is undamaged and complete).

---

### 3. Black November Sale — Special Return Conditions ⚠️

Items purchased during the annual **"Black November" promotional sale event** are subject to modified terms:

- **Extended Return Window:** Customers have **45 calendar days** from the confirmed delivery date (instead of the standard 30 days).
- **Mandatory Restocking Fee:** A **15% restocking fee** is applied to **all** Black November returns, regardless of whether the item is opened or unopened. This fee is non-negotiable and is automatically deducted from the refund amount.
- **Example:** A $200 item purchased during Black November and returned within 45 days will incur a $30 restocking fee, resulting in a $170 refund.

> **AI Agent Note:** Do not conflate the standard 10% restocking fee with the Black November 15% fee. They are separate rules and the Black November fee supersedes the standard fee for qualifying orders.

---

### 4. Non-Returnable & Non-Refundable Items

The following categories are **strictly non-refundable under all circumstances**:

| Category | Reason |
|---|---|
| **Open-box software licenses / activation codes** | Digital delivery; license activated on opening |
| Consumables (replacement tips, ear cushions after use) | Hygiene / single-use |
| Custom-engraved or personalized products | Cannot be resold |
| Items damaged by the customer (physical damage, liquid exposure outside warranty) | User damage |
| Products with removed serial number stickers | Cannot be authenticated |

> **Critical Rule:** Even if software was purchased during Black November, if the box has been opened and the activation key revealed or used, it is **non-refundable**. The 45-day window does not override the open-box software rule.

---

### 5. Return Shipping

- **Domestic (within India):** AuraGear provides a prepaid return shipping label for defective or incorrect items. For buyer's-remorse returns, the customer bears the return shipping cost.
- **International Returns:** Customers are responsible for all return shipping costs and any applicable customs duties. AuraGear does not reimburse international return shipping fees.

---

### 6. Exchange Policy

Exchanges for the same product (different color/size) are processed within the standard return window at no fee. Exchanges for a different product model are treated as a return followed by a new purchase.

---

### 7. How to Initiate a Return

1. Log in to your AuraGear account at auragear.com.
2. Navigate to **Orders → Select Order → Request Return**.
3. Select the return reason from the dropdown menu.
4. Print the return authorization slip and include it in the package.
5. Drop off at any authorized courier partner location.

For assistance, contact support@auragear.com or call 1800-AURA-123 (toll-free, India).

---
---

# DOCUMENT 2

```
Document ID:     AG-2001
Department:      Product Support / Hardware
Last Updated:    2026-02-03
Confidentiality: Public
```

## AuraPulse Smartwatch — Troubleshooting Guide

### Supported Models
This guide applies to: **AuraPulse SE**, **AuraPulse Pro**, and **AuraPulse Ultra** (Firmware 3.x and above).

---

### Issue 1: Screen Flickering

**Symptoms:** The display intermittently flashes, goes dark for a split second, or shows horizontal/vertical lines during normal use.

**Common Causes:**
- Temporary GPU render buffer overflow (software-level)
- Corrupted display cache from a failed OS micro-update
- Low battery (below 10%) causing voltage fluctuation to the display module

**Resolution Steps:**

**Step 1 — Check Battery Level**
Ensure the watch has at least 20% battery. Flickering that occurs exclusively below 10% battery is normal hardware behavior and not a defect. Charge the device and observe.

**Step 2 — Perform a Soft Reset** ✅ **(Recommended First Action)**
> A Soft Reset restarts the operating system without erasing any user data, settings, health history, or paired device configurations.

**How to perform a Soft Reset:**
1. Press and **hold the Power button for 10 seconds**.
2. The AuraGear logo will appear on the screen.
3. Release the button and allow the watch to reboot (approx. 30–45 seconds).
4. Observe the display for 10–15 minutes post-reboot.

In **~85% of screen flickering cases**, the Soft Reset resolves the issue permanently.

**Step 3 — Update Firmware**
If flickering persists after the Soft Reset, check for a pending firmware update via the AuraPulse companion app (iOS/Android → AuraPulse → Device Settings → Firmware Update).

**Step 4 — Perform a Hard Reset** ⚠️ **DATA LOSS WARNING**
> A Hard Reset (also called Factory Reset) **permanently erases ALL data** from the watch, including: health and fitness history, custom watch faces, saved workouts, paired Bluetooth devices, and all user preferences. This action is **irreversible**.

**How to perform a Hard Reset:**
1. Press and **hold the Power button AND the Volume Down button simultaneously for 12 seconds**.
2. A warning screen will appear: *"Factory Reset — All data will be erased."*
3. Confirm by pressing the Power button once.
4. The watch will reset and display the initial setup screen.

> **AI Agent Note — CRITICAL:** A customer asking "how do I reset my watch to fix flickering?" should be guided to the **Soft Reset first** (Power button 10s). Only escalate to Hard Reset if Soft Reset and firmware update have both failed AND the customer has been warned about data loss and explicitly consents to proceed.

---

### Issue 2: Sync Failures (Watch Not Syncing with App)

**Symptoms:** Health data, notifications, or activity logs are not transferring between the AuraPulse watch and the companion mobile app.

**Possible Causes:**
- Bluetooth connection interference or cache corruption
- Outdated companion app version
- Revoked location/Bluetooth permissions on the phone
- Multiple paired devices causing conflict

**Resolution Steps:**

**Step 1 — Verify Bluetooth Is Active**
Ensure Bluetooth is enabled on the phone and the watch is within 10 meters (30 ft) of the phone.

**Step 2 — Force Close and Reopen the App**
On iOS: swipe up from the home bar and swipe the AuraPulse app upward. On Android: go to Recent Apps and close the AuraPulse app. Reopen and attempt sync.

**Step 3 — Forget and Re-pair the Device**
1. On the phone, go to **Bluetooth Settings → Find "AuraPulse [Model]" → Forget/Unpair**.
2. On the watch, go to **Settings → Connections → Unpair Phone**.
3. Re-pair from scratch by opening the AuraPulse app and selecting **Add New Device**.

**Step 4 — Check App Permissions**
Navigate to **Phone Settings → Apps → AuraPulse App → Permissions**. Ensure the following are granted:
- Location (required for Bluetooth LE scanning on Android)
- Bluetooth
- Notifications
- Background App Refresh (iOS)

**Step 5 — Reinstall the App**
Uninstall the AuraPulse app completely and reinstall from the App Store or Google Play. Note: Locally cached data not yet synced to AuraCloud will be lost.

**Step 6 — Soft Reset the Watch**
Perform the Soft Reset as described in Issue 1, Step 2.

**If none of the above steps resolve the sync issue**, escalate to Tier 2 hardware support. The issue may indicate a faulty Bluetooth antenna, which is covered under the standard manufacturer's warranty.

---

### General Notes for Support Agents

- Always ask the customer to confirm their **firmware version** before troubleshooting (watch → Settings → About → Firmware Version).
- AuraPulse SE does not support cellular; Sync Failure on SE models is always Bluetooth-related, never cellular.
- AuraPulse Ultra supports satellite sync; if Bluetooth sync fails but satellite data is present, the issue is app-side, not hardware-side.

---
---

# DOCUMENT 3

```
Document ID:     AG-3001
Department:      Warranty & Post-Sales
Last Updated:    2026-01-28
Confidentiality: Public
```

## AuraGear Warranty Tiers — Standard vs. AuraCare+

### Introduction

All AuraGear products ship with the **Standard Limited Warranty**. Customers may optionally upgrade to **AuraCare+** within 60 days of purchase for enhanced coverage. This document outlines the precise scope, limitations, and claim procedures for both tiers.

---

### Tier 1: Standard Limited Warranty

**Coverage Duration:** 1 year from the original date of purchase.

**What Is Covered:**
- Manufacturing defects in materials and workmanship
- Hardware component failures that occur under normal use conditions
- Dead-on-arrival (DOA) units (must be reported within 7 days of delivery)
- Battery defects where capacity drops below 80% within the first year under normal charging cycles

**What Is NOT Covered:**
- Physical damage (cracked screens, bent frames, broken ports)
- Liquid or moisture damage of any kind
- Damage resulting from unauthorized repairs or modifications
- Normal wear and tear (scratched surfaces, faded paint, worn-out bands)
- Damage caused by third-party accessories not certified by AuraGear
- Cosmetic damage that does not affect functionality

**Claim Process:** Customer submits a warranty claim via auragear.com/warranty, ships the device (prepaid label provided), and receives a repaired or replacement unit within 10–14 business days.

---

### Tier 2: AuraCare+ (Premium Protection Plan)

**Coverage Duration:** 2 years from the original date of purchase (extends the standard 1-year coverage by 1 additional year).

**Cost:** AuraCare+ is priced per product category:
- Smartwatches: $49/year or $89 for 2 years
- Earbuds & Headphones: $29/year or $49 for 2 years
- Laptops & Tablets: $99/year or $179 for 2 years

**What Is Covered (in addition to all Standard Warranty items):**
- One (1) screen replacement per coverage year at no additional cost
- Accidental damage from drops (up to two incidents per year)
- **Accidental water/liquid damage — with strict conditions (see below)**
- Priority repair turnaround (5–7 business days instead of 10–14)
- Free express shipping for both outbound and return of repair units

---

### ⚠️ Water Damage Coverage — Critical Conditions (AuraCare+ Only)

AuraCare+ covers accidental water/liquid damage **only when ALL of the following conditions are simultaneously met:**

| Condition | Requirement |
|---|---|
| **Depth** | The device was submerged to a depth of **less than 2 meters** |
| **Duration** | The device was submerged for **less than 30 minutes** |
| **Incident Type** | The exposure was **accidental** (not intentional submersion for swimming, diving, etc.) |
| **Device Eligibility** | The device has an IP rating of IP67 or higher |

**If ANY of these conditions is not met, the water damage claim will be denied, even under AuraCare+.**

> **AI Agent Trap Scenario Examples:**
> - A customer says their AuraPulse Pro fell into a 1-meter-deep pool and they retrieved it after 45 minutes → **DENIED** (duration exceeds 30 minutes, even though depth is under 2 meters).
> - A customer intentionally wore their watch while snorkeling at 1.5 meters → **DENIED** (intentional submersion).
> - A customer dropped their watch into a sink for 20 minutes at less than 0.5 meters depth → **APPROVED** (both conditions met, accidental).
> - A customer's watch fell into water of unknown depth for 10 minutes → Agent must ask the customer to estimate the depth before approving.

---

### AuraCare+ Enrollment

To enroll in AuraCare+ after purchase:
1. Go to auragear.com/auracareplus.
2. Enter your product serial number and order ID.
3. Enrollment must be completed **within 60 days of the original purchase date**. Enrollments after 60 days are not accepted under any circumstances.

---

### Warranty Claim Escalation

Claims denied at the agent level may be escalated to the **Warranty Review Board** by the customer submitting a written appeal via email to warranty-appeals@auragear.com within 30 days of denial. The Board's decision is final.

---
---

# DOCUMENT 4

```
Document ID:     AG-4001
Department:      Logistics & Fulfillment
Last Updated:    2026-02-10
Confidentiality: Internal
```

## International Shipping & Customs Protocol

### Scope

This document covers AuraGear's shipping and customs handling procedures for international orders shipped from our primary fulfillment hub in Singapore. It covers three key regions: the **European Union (EU)**, the **United Kingdom (UK)**, and **India**. All shipping is fulfilled via AuraGear's contracted logistics partners (DHL Express and FedEx International Priority).

---

### 1. European Union (EU) — 27 Member States

**Incoterms:** DDP (Delivered Duty Paid)

AuraGear bears all import duties, VAT, and customs clearance fees for shipments to EU member states. The customer pays only the product price and shipping fee shown at checkout. No additional charges will be levied at the point of delivery.

**Delivery Timeline:** 5–8 business days from dispatch.

**Restricted Items for EU Shipping:**
- Lithium battery standalone shipments exceeding 100Wh must include IATA-compliant labeling (see AG-9001).
- Products subject to EU REACH chemical regulations (e.g., certain cable materials) may require additional compliance documentation. The logistics team handles this automatically.

**VAT Note:** VAT is calculated and collected at checkout based on the destination country's VAT rate. EU customers will see this broken out on their invoice.

---

### 2. United Kingdom (UK)

**Incoterms:** DDP (Delivered Duty Paid)

Similar to EU, AuraGear pays all UK customs duties and import VAT (UK VAT rate: 20%) on behalf of the customer. The price shown at checkout is the final all-inclusive price. No customs charges will appear on delivery.

**Delivery Timeline:** 4–6 business days from dispatch.

**Post-Brexit Note:** The UK is no longer part of the EU customs union. UK and EU shipments are processed separately. A customer returning a product from the UK follows UK-specific return shipping procedures (DHL UK Returns Portal), not the EU procedure.

**UKCA Compliance:** All AuraGear electronic products sold in the UK carry UKCA (UK Conformity Assessed) markings, as required by UK law post-Brexit.

---

### 3. India 🇮🇳

**Incoterms:** DAP (Delivered At Place) — **Customer Pays IGST**

> ⚠️ **Critical Difference from EU/UK:** Unlike shipments to the EU and UK, AuraGear does **NOT** pay customs duties or taxes for shipments to India. Indian customers are responsible for paying **IGST (Integrated Goods and Services Tax)** upon delivery or customs clearance.

**How It Works:**
1. The customer places an order and pays the product price + international shipping fee at checkout.
2. When the shipment arrives at Indian customs, the customer (or their customs broker) will receive a notification from the courier (DHL/FedEx) with the IGST amount due.
3. The customer must pay the IGST directly to the courier before the parcel is released for final delivery.
4. Typical IGST rate on consumer electronics: **18%** (subject to change per Indian GST Council decisions).

**Delivery Timeline:** 7–12 business days from dispatch (including customs processing time, which can vary significantly).

**Key Agent Instruction:** When an Indian customer reports "my package is stuck" or "I'm being asked to pay extra money at delivery," the agent should explain the IGST obligation and confirm this is standard procedure, not a scam. Provide the DHL/FedEx tracking reference and advise the customer to pay the IGST charge shown on the courier's notification.

---

### 4. Countries Not Currently Served

AuraGear does not currently ship directly to: Russia, North Korea, Iran, Belarus, Myanmar, Cuba, or any country subject to OFAC sanctions. Orders placed with shipping addresses in these countries will be automatically cancelled and refunded.

---

### 5. Customs Documentation

All international shipments include:
- Commercial Invoice (3 copies)
- Packing List
- Certificate of Origin (Singapore)
- Airway Bill

For shipments containing lithium batteries, an MSDS (Material Safety Data Sheet) is also included per IATA regulations.

---

### 6. Lost or Damaged in Transit — International

For international orders lost or damaged in transit:
- AuraGear files the insurance claim on the customer's behalf.
- Replacement or refund is issued within 10 business days of the courier confirming the loss/damage.
- Customers do not need to open their own dispute with the courier.

---
---

# DOCUMENT 5

```
Document ID:     AG-5001
Department:      Trust & Safety / Legal
Last Updated:    2026-01-20
Confidentiality: Internal
```

## Identity Verification & Privacy Policy (GDPR/CCPA Compliant)

### Purpose

This document outlines AuraGear's procedures for customer identity verification during account recovery and sensitive account modification actions. It also summarizes our data privacy commitments under GDPR (EU/UK) and CCPA (California, USA).

---

### 1. Standard Identity Verification (Low-Risk Actions)

For routine actions such as checking order status, updating shipping addresses, or requesting returns, the customer must verify their identity via **two of the following**:

- Email address on the account
- Phone number on the account
- Last 4 digits of the payment method used for the most recent order
- Date of birth (if provided at account creation)

---

### 2. High-Risk Account Modifications

The following actions are classified as **high-risk** and require elevated verification:

| Action | Why High-Risk |
|---|---|
| Changing the registered email address | Could lock the true owner out of their account |
| Changing the registered phone number | Bypasses SMS 2FA |
| Requesting a full account data export | Contains sensitive purchase and personal data |
| Initiating a chargeback dispute flag reversal | Financial impact |
| Removing all 2FA methods simultaneously | Creates account vulnerability |

---

### 3. High-Risk Verification Methods ⚠️

For all high-risk actions, the customer must provide **ONE of the following**:

**Option A — Security Key (Preferred)**
The customer must have previously registered a FIDO2 hardware security key (e.g., YubiKey) with their AuraGear account. They use this key to cryptographically authenticate the request through the AuraGear web portal.

**Option B — Photo ID with Hidden 4-Digit Code**

> This is the primary method for customers who have not registered a security key.

Process:
1. The customer submits a government-issued photo ID (passport, national ID card, driver's license).
2. The ID is cross-referenced against account registration data (name, date of birth).
3. The customer **must also provide the hidden 4-digit security code** that was displayed once — and only once — during their account creation. This code is never stored by AuraGear in plain text and cannot be recovered by support staff.
4. If the customer cannot produce the 4-digit code, the high-risk action cannot be completed via chat/phone support. The customer must submit a notarized identity affidavit to legal@auragear.com and wait for the Trust & Safety team's manual review (3–5 business days).

> **AI Agent Instruction:** Never confirm, hint at, or attempt to recover the 4-digit security code for a customer. Never tell the customer what their code "might be." If the customer does not have it, direct them to the notarized affidavit process.

---

### 4. Data Retention Policy

| Data Type | Retention Period |
|---|---|
| Order and transaction records | 7 years (legal/tax compliance) |
| Account profile data | Duration of account + 2 years post-deletion |
| Support chat transcripts | 3 years |
| Browsing/session data | 13 months |
| Health data (AuraPulse) | Until deleted by user or 5 years post account closure |

---

### 5. GDPR Rights (EU/UK Customers)

EU and UK customers have the following rights under GDPR:

- **Right to Access:** Request a full export of personal data (subject to high-risk verification, see Section 3).
- **Right to Erasure ("Right to be Forgotten"):** Request deletion of account and associated data. Note: Transaction records retained for 7 years per legal requirement cannot be deleted.
- **Right to Portability:** Receive data in a machine-readable format (JSON/CSV).
- **Right to Object:** Opt out of marketing communications and profiling at any time.
- **Data Breach Notification:** In the event of a breach affecting personal data, AuraGear will notify affected users within 72 hours of becoming aware of the breach, in compliance with GDPR Article 33.

---

### 6. CCPA Rights (California Customers)

California residents under CCPA have the right to:
- Know what personal information is collected
- Delete personal information (with exceptions for legal retention)
- Opt-out of the sale of personal information (AuraGear does not sell customer data to third parties)
- Non-discrimination for exercising CCPA rights

---

### 7. Data Privacy Requests

Submit all GDPR/CCPA requests to: **privacy@auragear.com**
Response time: Within 30 days (extendable to 60 days for complex requests with notice).

---
---

# DOCUMENT 6

```
Document ID:     AG-6001
Department:      Product Development / Strategy
Last Updated:    2026-03-01
Confidentiality: CONFIDENTIAL — INTERNAL ONLY
```

## Product Launch Roadmap 2026 — Internal Only

> # 🔴 CONFIDENTIAL — DO NOT SHARE WITH CUSTOMERS OR EXTERNAL PARTIES
> This document contains forward-looking product information that has not been publicly announced. Sharing this information externally constitutes a breach of the AuraGear Employee NDA and may result in disciplinary action, including termination. This document is accessible to employees at Director level and above, and to specifically cleared product teams.

---

### Q2 2026 — Planned Launches

**AuraBeam Projector (Codename: SUNSPOT)**
- A portable 4K laser-phosphor micro-projector with built-in AuraOS.
- Estimated MSRP: $799 (32GB internal) / $999 (128GB internal).
- Target launch: Q3 2026 (July–September window, exact date TBD).
- Key differentiator: 120-inch projection at 1.2m throw distance; integrated AuraCloud streaming; battery life 4 hours (projection) / 8 hours (audio-only mode).
- PR/Marketing embargo: **All product details remain under NDA until the official press release date.**

**AuraPulse 3 Series (Codename: MARATHON)**
- Next-generation smartwatch with satellite GPS, 10-day battery, and blood glucose monitoring (regulatory approval pending in US and EU).
- Estimated MSRP: $349 (base) / $499 (Ultra).
- Target launch: Q4 2026.

**AuraBuds Max V2**
- Over-ear headphones with ANC 3.0 and spatial audio. Successor to AuraBuds Max.
- Estimated MSRP: $329.
- Target launch: Q4 2026.

---

### Q3–Q4 2026 — Pipeline (Exploratory / Not Confirmed)

- **AuraTab Pro 2** — 12.9" OLED tablet with optional cellular. Under active development.
- **AuraGear SmartHome Hub** — Integration platform for AuraGear IoT products. Concept stage.

---

### Competitive Intelligence Notes (Internal Only)

[Content redacted from this knowledge base excerpt — see separate Competitive Intel folder on internal SharePoint]

---

> ## AI AGENT INSTRUCTION — MANDATORY
> If a customer asks about any product listed in this document — including but not limited to the AuraBeam Projector, AuraPulse 3, AuraBuds Max V2, or any "upcoming" AuraGear products — the AI agent **must refuse to confirm or deny the existence of these products**. The correct response is:
> *"I don't have information about upcoming or unreleased products. For the latest product announcements, please follow AuraGear's official channels at auragear.com/news or our official social media."*
> Under no circumstances should the agent reveal pricing, specifications, codenames, or launch timelines for any product in this roadmap.

---
---

# DOCUMENT 7

```
Document ID:     AG-7001
Department:      Software & Services
Last Updated:    2026-01-30
Confidentiality: Public
```

## Subscription Service: AuraCloud Storage Tiers

### Overview

AuraCloud is AuraGear's integrated cloud storage and sync platform, built to back up and synchronize data from all AuraGear devices — including AuraPulse health data, AuraBuds EQ settings, and AuraGear device configurations.

---

### Tier Comparison Table

| Feature | Free | Pro ($9.99/mo) | Family ($14.99/mo) |
|---|---|---|---|
| Total Storage | 15 GB | 1 TB (1,000 GB) | 5 TB (shared across members) |
| High-Speed Sync Quota | 5 GB | 100 GB/month | 100 GB/month per member |
| Number of Users | 1 | 1 | Up to 6 members |
| Device Backup | Up to 2 devices | Unlimited devices | Unlimited devices per member |
| AuraPulse Health Backup | Last 30 days | Full history | Full history per member |
| Priority Sync | ❌ | ✅ | ✅ |
| Offline Playlist Caching | ❌ | ✅ (up to 50GB) | ✅ (up to 50GB per member) |
| Cross-Device Sync Speed | Standard | Priority | Priority |
| AuraGear Support Tier | Standard | Priority Chat | Priority Chat |

---

### ⚠️ High-Speed Sync — Important Clarification

> This is a frequently misunderstood feature. Read carefully.

**Pro plan users receive 1 TB of total storage.** However, data transfer to/from AuraCloud uses two different speed tiers:

- **High-Speed Sync:** Files uploaded or downloaded using AuraCloud's maximum bandwidth allocation. Capped at **100 GB per calendar month** for Pro users. Once the 100 GB High-Speed Sync quota is exhausted, all syncing continues at **Standard Speed** (throttled to ~5 Mbps) for the remainder of the month. The quota resets on the 1st of each calendar month.
- **Standard Speed Sync:** Throttled transfers. All 1 TB of storage remains accessible; only the speed is reduced.

> **AI Agent Note:** A Pro user with 800 GB of data is NOT limited to 100 GB of usable storage. They have 1 TB of storage available. The 100 GB limit applies only to high-speed transfer bandwidth per month. If a customer complains that "syncing has slowed down," ask if they have exceeded their monthly High-Speed Sync quota before escalating to a technical issue.

---

### Family Plan Details

- The Family plan administrator (the account that purchased the plan) can invite up to **5 additional members** (6 total).
- Each member gets their own private storage partition. Members cannot access each other's files.
- The 5 TB total is shared across all members. If one member uses 4 TB, the remaining 5 members share 1 TB.
- Each member individually gets the 100 GB/month High-Speed Sync quota.
- Family members must have individual AuraGear accounts. Sub-accounts under a parent account are not supported.

---

### Billing and Cancellation

- Pro and Family plans are billed monthly or annually (annual billing saves ~15%).
- Cancellation takes effect at the end of the current billing period. Data is not immediately deleted.
- **Data Retention After Cancellation:** AuraGear retains data for **30 days** after the subscription end date. After 30 days, data exceeding the Free tier limit (15 GB) is permanently deleted. The customer will receive email warnings at 7 days and 3 days before deletion.
- Downgrading from Family to Pro is immediate; members beyond the account holder are removed instantly from the plan, though their data is retained for 30 days under the grace policy.

---

### Upgrading Mid-Cycle

Upgrades from Free → Pro or Pro → Family are prorated. The customer is charged the difference for the remaining days in the billing cycle at the time of upgrade.

---
---

# DOCUMENT 8

```
Document ID:     AG-8001
Department:      Customer Loyalty / Marketing
Last Updated:    2026-02-14
Confidentiality: Public
```

## AuraPoints Loyalty Program — Rules & Redemption

### Program Overview

AuraPoints is AuraGear's customer loyalty program, rewarding customers for purchases, product reviews, referrals, and engagement activities. Points can be redeemed for discounts on future AuraGear purchases.

---

### Earning AuraPoints

| Activity | Points Earned |
|---|---|
| Purchases on auragear.com or AuraGear App | **1 point per $1 (USD) spent** |
| Purchases in AuraGear retail stores | 1 point per $1 spent |
| Verified product review submission | 50 points per review (max 1 per product) |
| Referral (friend makes first purchase) | 200 points per successful referral |
| AuraCare+ enrollment | 100 bonus points |
| Birthday bonus (account must be 30+ days old) | 500 points on birthday month |

**Notes on Purchase Points:**
- Points are calculated on the **final paid amount** after all discounts and coupons. If a $200 item is purchased with a $50 coupon, points are awarded on $150.
- Points are **not earned** on: shipping fees, taxes, gift card purchases, or AuraCloud subscription fees.
- Points for a purchase are held in **Pending** status until the return window closes (30 days, or 45 days for Black November purchases). This prevents point gaming via purchase-and-return.
- If a purchase is returned, the associated points are deducted from the account balance, even if they were already converted from Pending to Active.

---

### Redeeming AuraPoints

- **Minimum redemption:** 500 points ($5 value)
- **Redemption rate:** 100 points = $1 discount
- Points can be applied at checkout on auragear.com or in-store.
- Points cannot be redeemed for cash, transferred between accounts, or used to purchase gift cards.
- A maximum of **5,000 points ($50)** can be redeemed per single transaction.

---

### ⚠️ Point Expiration Policy — Critical Rule

> Points expire after **12 consecutive months of account inactivity.**

**Definition of "Activity":**
- Any qualifying purchase
- Any product review submission
- Any referral redemption
- Logging into the AuraGear account (auragear.com or mobile app)

> **Trap for AI:** Simply logging in to the AuraGear account DOES count as activity and resets the 12-month inactivity clock. A customer who is worried about points expiring can simply log in to preserve them — they do not need to make a purchase.

**Important Nuance:**
- The 12-month clock counts from the **last activity date**, not from the date points were earned.
- If a customer earned 1,000 points in January 2025 and last logged in to their account in March 2025, and then takes no action until April 2026 (13 months later), all points expire — including the ones earned in January 2025.

---

### AuraPoints Tiers

| Tier | Annual Spend | Benefit |
|---|---|---|
| Silver | $0–$499 | Base earning rate |
| Gold | $500–$1,499 | 1.25x point multiplier |
| Platinum | $1,500+ | 1.5x point multiplier + free express shipping |

Tier status is recalculated on January 1st of each year based on spending in the prior calendar year.

---

### Points and Promotions

- Double-points promotional events do not stack with the Platinum tier multiplier. The higher value applies.
- Points earned during a promotional period are still subject to the standard expiration rules.
- AuraPoints cannot be combined with AuraGear employee discounts.

---
---

# DOCUMENT 9

```
Document ID:     AG-9001
Department:      Logistics / Compliance
Last Updated:    2026-01-12
Confidentiality: Internal
```

## Dangerous Goods & Battery Safety — Lithium-Ion Handling Protocol

### Regulatory Scope

This document governs the handling, packaging, storage, and shipment of AuraGear products containing lithium-ion (Li-ion) and lithium polymer (LiPo) batteries. All procedures comply with:

- **IATA Dangerous Goods Regulations (DGR)** — 65th Edition
- **IMDG Code** (sea freight, where applicable)
- **UN Recommendations on the Transport of Dangerous Goods (UN Model Regulations)**

---

### 1. Battery Classification

| Product Type | Battery Capacity | UN Number | Packing Instruction |
|---|---|---|---|
| AuraPulse Smartwatches | < 2 Wh (all models) | UN 3481 | PI 967, Section II |
| AuraBuds Earbuds | < 1 Wh per cell | UN 3481 | PI 967, Section II |
| AuraBuds Max (over-ear) | 5 Wh | UN 3481 | PI 967, Section II |
| AuraTab Tablets | 38–42 Wh | UN 3481 | PI 967, Section II |
| AuraGear Laptop | 72 Wh | UN 3481 | PI 967, Section IA/IB |
| Standalone Replacement Batteries | Varies | UN 3480 | PI 965 |

> **Note:** UN 3481 = Lithium-ion batteries **contained in equipment**. UN 3480 = Lithium-ion batteries **alone (standalone)**. This distinction is critical for labeling and airline approval.

---

### 2. Air Freight Restrictions

**State of Charge (SoC) Requirement:**
- All lithium batteries in products shipped via air must be at or below **30% state of charge** at the time of shipment.
- Standalone lithium battery shipments (spare/replacement batteries) are **prohibited in passenger aircraft cargo holds** if they exceed 100 Wh. They may only travel on cargo aircraft under specific conditions.

**Quantity Limits per Shipment:**
- Section II compliance: No more than **8 batteries or 8 devices** per package when shipped under Section II rules.
- Exceeding this limit requires full Section I compliance documentation (Shipper's Declaration for Dangerous Goods).

---

### 3. Packaging Requirements

All lithium battery shipments must meet the following:

- **Inner packaging:** Batteries/devices must be individually separated to prevent short circuits (e.g., placed in original retail packaging, or individually bagged in antistatic material).
- **Outer packaging:** Must be rigid, pass 1.2m drop test under UN standards.
- **Labeling:** Must display the Lithium Battery Handling Mark (UN 3480/3481 label as applicable), Class 9 hazmat label (Section I only), and "THIS SIDE UP" arrows.

---

### 4. Customer-Facing Battery Safety Instructions

The following safety guidelines must be provided to customers upon request and are included in all product packaging:

- **Do NOT puncture, crush, or disassemble** the battery or any device containing a lithium battery.
- **Do NOT expose** to temperatures above 60°C (140°F) or submerge in water for extended periods.
- **Do NOT charge** with a non-certified or third-party charger not explicitly approved by AuraGear. Using uncertified chargers voids the warranty.
- **Swollen batteries** are a safety hazard. If you notice your device's back cover bulging or swelling, immediately discontinue use and contact AuraGear support. **Do not attempt to charge or use a swollen battery device.**
- In the event of a battery fire, use a Class D fire extinguisher or sand. **Do NOT use water.**
- Dispose of lithium batteries at certified e-waste facilities. Do NOT place in household trash or recycling bins.

---

### 5. Damaged Battery Returns

If a customer needs to return a device with a **damaged, swollen, or leaking battery:**

1. Do **not** use standard return label; escalate to the Dangerous Goods Return team (dg-returns@auragear.com).
2. A specialist will ship a UN-certified, non-conductive foam-lined return kit to the customer.
3. The customer should store the device in a cool, dry, well-ventilated area away from flammable materials while awaiting the return kit.
4. Standard courier services (DHL consumer, USPS, India Post) cannot accept packages with damaged lithium batteries. Only approved hazmat couriers are used.

---
---

# DOCUMENT 10

```
Document ID:     AG-10001
Department:      Customer Experience / Operations
Last Updated:    2026-02-20
Confidentiality: Internal
```

## Customer Escalation Matrix — Human Handoff Rules

### Purpose

This document defines the precise conditions under which an AI customer support agent or Tier 1 support representative must escalate a customer interaction to a **Senior Specialist**, **Team Lead**, or **Legal/Specialized Team**. The goal is to ensure that complex, high-risk, or sensitive situations receive appropriate human attention while minimizing unnecessary escalations that slow resolution times.

---

### Tier Structure

| Tier | Role | Handles |
|---|---|---|
| Tier 0 | AI Agent | Routine inquiries, FAQ, policy explanations, basic troubleshooting |
| Tier 1 | General Support Rep | Standard returns, warranty claims, account issues |
| Tier 2 | Senior Specialist | Complex cases meeting escalation criteria (see below) |
| Tier 3 | Team Lead / Manager | Tier 2 escalations, customer VIP cases, SLA breaches |
| Specialized | Legal, Trust & Safety, Finance | Legal threats, fraud, large orders, GDPR requests |

---

### Mandatory Escalation Triggers

The following conditions **require immediate escalation** and the AI agent or Tier 1 rep must **never attempt to resolve independently:**

---

#### 1. Legal Action Threats

**Trigger:** Customer explicitly states any of the following (or clear equivalents):
- "I will sue AuraGear"
- "I am contacting my lawyer"
- "I'm filing a complaint with the consumer court / FTC / Trading Standards"
- "This is going to court"
- "I'm reporting you to the DGCA / regulatory authority"

**Action:** Immediately acknowledge the customer, cease attempting to resolve the dispute, and transfer to the **Legal Response Team**.

> **Script:** *"I understand your frustration and I want to make sure you're speaking with the right person. I'm connecting you now with our Senior Escalations Team, who is best equipped to help with your situation."*

> **AI Agent Note:** Do NOT argue with the customer, attempt to dissuade them from legal action, or offer unauthorized settlements. Simply acknowledge and escalate.

---

#### 2. Three Consecutive Failed Troubleshooting Attempts

**Trigger:** The same technical issue has not been resolved after **three distinct troubleshooting sessions** with the support team (AI or human), regardless of whether those sessions occurred in one interaction or across multiple contacts.

**Criteria for counting a "failed attempt":**
- A complete troubleshooting sequence (not just one step) was followed.
- The customer confirmed the issue persisted after completing the steps.
- The interaction was logged in the support CRM with a resolution outcome of "Unresolved."

**Action:** Escalate to Tier 2 Senior Specialist. The specialist has authority to approve product replacements without requiring further troubleshooting.

> **AI Agent Note:** If you can see in the customer's case history that two prior troubleshooting sessions for the same issue are logged as "Unresolved," treat the current session as the third attempt and escalate **after** this session's troubleshooting also fails. Do not pre-emptively escalate before attempting; only escalate after the third failure is confirmed.

---

#### 3. High-Value Orders (Exceeding $5,000)

**Trigger:** Any support request — return, exchange, warranty claim, shipping issue, or dispute — related to an order or cumulative set of products in a single transaction with a **total order value exceeding $5,000 USD**.

**Rationale:** High-value order resolutions carry significant financial risk and require Senior Specialist authorization to approve refunds, replacements, or accommodations.

**Action:** Transfer to Senior Specialist immediately. Do not attempt to process the return or refund independently.

> **Nuance:** If a customer has multiple separate orders each under $5,000 but totaling more than $5,000 across all orders, this threshold does NOT apply — the $5,000 trigger is per single transaction/order, not cumulative lifetime value.

---

#### 4. Fraud Suspicion or Account Compromise

**Trigger:** The interaction shows indicators of potential fraud or unauthorized account access, including but not limited to:
- Request to change account details inconsistent with the verified customer's history
- Multiple return requests on different accounts from the same address
- Pressure to bypass identity verification
- Customer claims unauthorized purchases they do not recognize

**Action:** Do not proceed. Transfer to the **Trust & Safety Team** immediately and follow the Identity Verification Protocol (see AG-5001).

---

#### 5. Vulnerable Customer Indicators

**Trigger:** The customer displays indicators of being in a vulnerable state — extreme emotional distress, mentions of personal crisis unrelated to the purchase, or language suggesting they may not be in a position to make informed decisions.

**Action:** With empathy, transfer to a human Team Lead. Do not attempt to continue a sales or resolution conversation.

---

### Escalation Procedure (Step-by-Step)

1. Inform the customer: *"I want to make sure you're connected with the best person to help you. Let me transfer you now."*
2. Log the escalation reason in the CRM case notes with timestamp.
3. Transfer the full conversation context to the receiving agent (do not require the customer to repeat their issue).
4. **Do not end the chat/call before confirming the Tier 2 agent has joined** (warm handoff required; cold transfer is prohibited for Tier 2+ escalations).

---

### SLA for Escalated Cases

| Tier | Initial Response SLA | Resolution SLA |
|---|---|---|
| Tier 2 (Senior Specialist) | 2 hours | 24 hours |
| Tier 3 (Team Lead) | 1 hour | 12 hours |
| Legal Response Team | 4 hours | 48 hours |
| Trust & Safety | 1 hour | 8 hours |

---

*End of AuraGear Internal Knowledge Base — 10 Documents*
*Document set compiled for RAG AI Training — Version 1.0*
