from pydantic import BaseModel, Field
from typing import List, Optional, Literal


# =========================================================
# ALLOWED ENUM-LIKE VALUES
# =========================================================

HandoffTarget = Literal[
    "tech_support_agent",
    "billing_agent",
    "security_agent",
    "shipping_agent"
]

IntentType = Literal[
    "technical_support",
    "billing_refund",
    "security_privacy",
    "shipping_logistics",
    "general_query"
]

IssueType = Literal[
    "device_not_working",
    "battery_issue",
    "firmware_issue",
    "refund_request",
    "warranty_claim",
    "shipping_delay",
    "customs_tax",
    "account_recovery",
    "privacy_request",
    "unknown"
]

CustomerSentiment = Literal[
    "calm",
    "frustrated",
    "angry",
    "abusive",
    "threatening"
]

PurchasePeriod = Literal[
    "black_november",
    "holiday_sale",
    "standard_period",
    "unknown"
]

RegionType = Literal[
    "india",
    "uk",
    "eu",
    "us",
    "other"
]


# =========================================================
# SPECIALIST AGENT OUTPUT
# =========================================================

class SpecialistAgentOutput(BaseModel):

    response: str = Field(
        description="Final customer-facing response"
    )

    sources: List[str] = Field(
        default_factory=list,
        description="Knowledge base document IDs used"
    )

    escalation_required: bool = Field(
        default=False,
        description="Whether escalation to human support is required"
    )

    escalation_reason: Optional[str] = Field(
        default=None,
        description="Reason for escalation if escalation_required is true"
    )


# =========================================================
# TRIAGE / MAIN AGENT DECISION
# =========================================================

class MainAgentOutput(BaseModel):

    handoff_target: Optional[HandoffTarget] = Field(
        default=None,
        description="Target specialist agent for delegation"
    )

    needs_handoff: bool = Field(
        default=True,
        description="Whether delegation to specialist is required"
    )

    updated_state: dict = Field(
        description="Updated shared session state"
    )

    direct_response: Optional[str] = Field(
        default=None,
        description="Direct response if no specialist handoff is required"
    )

    escalation_required: bool = Field(
        default=False,
        description="Whether escalation is required"
    )

    escalation_reason: Optional[str] = Field(
        default=None,
        description="Reason for escalation"
    )

    reasoning_summary: Optional[str] = Field(
        default=None,
        description="Short internal routing summary for observability"
    )


# =========================================================
# SHARED SESSION STATE
# =========================================================

class SupportSessionState(BaseModel):

    session_id: str = Field(
        description="Unique support session identifier"
    )

    intent: Optional[IntentType] = Field(
        default=None,
        description="Primary detected customer intent"
    )

    product_name: Optional[str] = Field(
        default=None,
        description="AuraGear product involved in issue"
    )

    issue_type: Optional[IssueType] = Field(
        default=None,
        description="Specific classified issue category"
    )

    escalation_required: bool = Field(
        default=False,
        description="Whether escalation has been triggered"
    )

    escalation_reason: Optional[str] = Field(
        default=None,
        description="Reason for escalation"
    )

    troubleshooting_attempts: int = Field(
        default=0,
        ge=0,
        le=10,
        description="Number of troubleshooting attempts performed"
    )

    customer_sentiment: Optional[CustomerSentiment] = Field(
        default=None,
        description="Detected customer sentiment"
    )

    region: Optional[RegionType] = Field(
        default=None,
        description="Customer region for policy/shipping handling"
    )

    purchase_period: Optional[PurchasePeriod] = Field(
        default=None,
        description="Purchase campaign or period classification"
    )

    extracted_entities: List[str] = Field(
        default_factory=list,
        description="Entities extracted from conversation"
    )