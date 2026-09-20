import streamlit as st
import pandas as pd


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="SmartCity Insight AI",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# PROJECT DATA
# ============================================================

PATTERNS = [
    {
        "Pattern": "Waterlogging near bus stops",
        "Complaint Count": 7,
        "Evidence IDs": "G001, G003, G006, G010, G017, G029, G036"
    },
    {
        "Pattern": "Drainage near markets",
        "Complaint Count": 3,
        "Evidence IDs": "G002, G007, G037"
    },
    {
        "Pattern": "Waste near markets",
        "Complaint Count": 6,
        "Evidence IDs": "G005, G009, G015, G020, G039, G046"
    },
    {
        "Pattern": "Non-working streetlights",
        "Complaint Count": 8,
        "Evidence IDs": "G004, G008, G016, G021, G028, G033, G040, G047"
    },
    {
        "Pattern": "Waterlogging near schools",
        "Complaint Count": 2,
        "Evidence IDs": "G011, G041"
    },
    {
        "Pattern": "Road damage / potholes",
        "Complaint Count": 7,
        "Evidence IDs": "G013, G014, G019, G026, G031, G038, G043"
    },
    {
        "Pattern": "Public transport issues",
        "Complaint Count": 5,
        "Evidence IDs": "G022, G023, G034, G044, G050"
    },
    {
        "Pattern": "Waterlogging near community halls",
        "Complaint Count": 2,
        "Evidence IDs": "G024, G048"
    },
    {
        "Pattern": "Drainage near community halls",
        "Complaint Count": 2,
        "Evidence IDs": "G025, G049"
    },
    {
        "Pattern": "Waste near schools",
        "Complaint Count": 2,
        "Evidence IDs": "G027, G032"
    },
    {
        "Pattern": "Traffic noise near markets",
        "Complaint Count": 2,
        "Evidence IDs": "G035, G045"
    }
]

patterns_df = pd.DataFrame(PATTERNS)


FACTORS = [
    {
        "Pattern": "Waterlogging near bus stops",
        "Possible Contributing Factors":
            "Drainage capacity; drainage design; stormwater management; possible blockages",
        "Evidence Strength": "Medium"
    },
    {
        "Pattern": "Drainage near markets",
        "Possible Contributing Factors":
            "Debris or waste in drains; structural damage; insufficient drainage capacity",
        "Evidence Strength": "Medium"
    },
    {
        "Pattern": "Waste near markets",
        "Possible Contributing Factors":
            "Collection frequency; available waste-management resources; increased waste generation",
        "Evidence Strength": "Medium"
    },
    {
        "Pattern": "Non-working streetlights",
        "Possible Contributing Factors":
            "Electrical faults; damaged infrastructure; maintenance issues; power supply problems",
        "Evidence Strength": "Medium"
    },
    {
        "Pattern": "Waterlogging near schools",
        "Possible Contributing Factors":
            "Drainage capacity; drainage design; stormwater management; possible blockages",
        "Evidence Strength": "Low"
    },
    {
        "Pattern": "Road damage / potholes",
        "Possible Contributing Factors":
            "Road maintenance; heavy traffic loads; construction quality",
        "Evidence Strength": "Medium"
    },
    {
        "Pattern": "Public transport issues",
        "Possible Contributing Factors":
            "Scheduling; fleet availability; staffing",
        "Evidence Strength": "Medium"
    },
    {
        "Pattern": "Waterlogging near community halls",
        "Possible Contributing Factors":
            "Drainage capacity; drainage design; stormwater management; possible blockages",
        "Evidence Strength": "Low"
    },
    {
        "Pattern": "Drainage near community halls",
        "Possible Contributing Factors":
            "Debris or waste in drains; structural damage; insufficient drainage capacity",
        "Evidence Strength": "Medium"
    },
    {
        "Pattern": "Waste near schools",
        "Possible Contributing Factors":
            "Collection frequency; available waste-management resources; waste generation during school hours",
        "Evidence Strength": "Medium"
    },
    {
        "Pattern": "Traffic noise near markets",
        "Possible Contributing Factors":
            "Traffic volume; noise barriers; surrounding urban conditions",
        "Evidence Strength": "Low"
    }
]

factors_df = pd.DataFrame(FACTORS)


INSIGHT_REPORT = [
    {
        "Issue": "Waterlogging",
        "Location": "Near bus stops",
        "Complaint Count": 7,
        "Observed Evidence":
            "Repeated reports of waterlogging near bus stops after rainfall",
        "Possible Contributing Factor":
            "Drainage capacity, design, stormwater management, or possible blockages",
        "Recommended Investigation":
            "Check drainage capacity, blockages, design, and maintenance records",
        "Important Limitation":
            "Possible factors are hypotheses and require real-world verification"
    },
    {
        "Issue": "Drainage",
        "Location": "Near markets",
        "Complaint Count": 3,
        "Observed Evidence":
            "Repeated reports of drainage-related complaints near markets",
        "Possible Contributing Factor":
            "Debris, structural damage, or insufficient drainage capacity",
        "Recommended Investigation":
            "Inspect drains, blockages, structural condition, and capacity",
        "Important Limitation":
            "Complaint reports do not prove the physical cause"
    },
    {
        "Issue": "Waste",
        "Location": "Near markets",
        "Complaint Count": 6,
        "Observed Evidence":
            "Repeated reports of waste accumulation near markets",
        "Possible Contributing Factor":
            "Collection frequency, resources, or increased waste generation",
        "Recommended Investigation":
            "Review collection schedules, service records, and waste-management resources",
        "Important Limitation":
            "Reported waste volume may not represent actual waste generation"
    },
    {
        "Issue": "Streetlights",
        "Location": "Multiple reported locations",
        "Complaint Count": 8,
        "Observed Evidence":
            "Repeated reports of non-working streetlights",
        "Possible Contributing Factor":
            "Electrical faults, infrastructure damage, maintenance, or power supply",
        "Recommended Investigation":
            "Inspect affected streetlights and review maintenance and power records",
        "Important Limitation":
            "Reports require physical verification"
    },
    {
        "Issue": "Waterlogging",
        "Location": "Near schools",
        "Complaint Count": 2,
        "Observed Evidence":
            "Repeated reports of waterlogging near schools after rainfall",
        "Possible Contributing Factor":
            "Drainage capacity, design, stormwater management, or possible blockages",
        "Recommended Investigation":
            "Inspect drainage systems and check for blockages and capacity issues",
        "Important Limitation":
            "Low evidence strength; further evidence is required"
    },
    {
        "Issue": "Road Damage",
        "Location": "Multiple reported locations",
        "Complaint Count": 7,
        "Observed Evidence":
            "Repeated reports of potholes or damaged road surfaces",
        "Possible Contributing Factor":
            "Road maintenance, traffic loads, or construction quality",
        "Recommended Investigation":
            "Inspect road conditions and review maintenance and construction records",
        "Important Limitation":
            "Possible contributing factors are not confirmed causes"
    },
    {
        "Issue": "Public Transport",
        "Location": "Multiple reported locations",
        "Complaint Count": 5,
        "Observed Evidence":
            "Reports of late buses, overcrowding, or inconsistent service",
        "Possible Contributing Factor":
            "Scheduling, fleet availability, or staffing",
        "Recommended Investigation":
            "Review schedules, fleet availability, and staffing information",
        "Important Limitation":
            "Service complaints require operational verification"
    },
    {
        "Issue": "Waterlogging",
        "Location": "Near community halls",
        "Complaint Count": 2,
        "Observed Evidence":
            "Repeated reports of waterlogging near community halls after rainfall",
        "Possible Contributing Factor":
            "Drainage capacity, design, stormwater management, or possible blockages",
        "Recommended Investigation":
            "Inspect drainage systems and verify reported blockages",
        "Important Limitation":
            "Low evidence strength; further evidence is required"
    },
    {
        "Issue": "Drainage",
        "Location": "Near community halls",
        "Complaint Count": 2,
        "Observed Evidence":
            "Repeated reports of drainage-related complaints near community halls",
        "Possible Contributing Factor":
            "Debris, structural damage, or insufficient drainage capacity",
        "Recommended Investigation":
            "Inspect drains and check structural condition and capacity",
        "Important Limitation":
            "Complaint reports do not prove the physical cause"
    },
    {
        "Issue": "Waste",
        "Location": "Near schools",
        "Complaint Count": 2,
        "Observed Evidence":
            "Repeated reports of waste accumulation near schools",
        "Possible Contributing Factor":
            "Collection frequency, resources, or waste generation during school hours",
        "Recommended Investigation":
            "Review collection schedules and waste-management resources",
        "Important Limitation":
            "Reported complaints do not establish the underlying cause"
    },
    {
        "Issue": "Traffic Noise",
        "Location": "Near markets",
        "Complaint Count": 2,
        "Observed Evidence":
            "Repeated reports of traffic noise near markets",
        "Possible Contributing Factor":
            "Traffic volume, noise barriers, or surrounding urban conditions",
        "Recommended Investigation":
            "Check traffic conditions and, where appropriate, measured noise levels",
        "Important Limitation":
            "Low evidence strength; further evidence is required"
    }
]

insight_df = pd.DataFrame(INSIGHT_REPORT)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("🏙️ SmartCity")
    st.subheader("Insight AI")

    st.divider()

    st.markdown("### 📌 Project")
    st.caption("SDG 11 — Sustainable Cities and Communities")

    st.divider()

    st.markdown("### 🔬 AI Pipeline")

    st.markdown(
        """
        **01** Information Extraction  
        **02** Complaint Classification  
        **03** Similar Grouping  
        **04** Pattern Detection  
        **05** Root-Cause Analysis  
        **06** Insight & Action Report
        """
    )

    st.divider()

    st.markdown("### 🤖 Responsible AI")

    st.caption(
        "AI suggestions support analysis. "
        "Human verification is required before action."
    )

    st.divider()

    st.caption("1M1B AI for Sustainability")
    st.caption("Virtual Internship Project")


# ============================================================
# MAIN HEADER
# ============================================================

st.title("🏙️ SmartCity Insight AI")

st.subheader(
    "AI-Powered Urban Grievance Pattern & Root-Cause Analyzer"
)

st.markdown(
    "Identify recurring complaint patterns, explore possible contributing "
    "factors, and support evidence-based human investigation."
)

# Native badges using columns
badge1, badge2, badge3, badge4 = st.columns(4)

with badge1:
    st.info("🤖 AI-Assisted")

with badge2:
    st.success("🌱 SDG 11")

with badge3:
    st.info("🔎 Pattern Analysis")

with badge4:
    st.warning("👤 Human Verified")


st.divider()


# ============================================================
# PROJECT OVERVIEW
# ============================================================

st.header("📋 Project Overview")

st.info(
    "SmartCity Insight AI analyzes synthetic urban grievance data to "
    "identify recurring complaint patterns, possible contributing factors, "
    "and areas requiring further investigation."
)

st.markdown(
    """
    **Project objective**

    Transform a collection of urban complaints into structured insights
    that can help humans understand recurring patterns.

    **Important:** The system is a decision-support prototype. It does not
    determine confirmed physical causes and does not make government decisions.
    """
)


# ============================================================
# DATA INPUT
# ============================================================

st.header("📁 Data Input")

st.write(
    "Upload the synthetic grievance dataset to begin the analysis."
)

uploaded_file = st.file_uploader(
    "Upload Dataset.csv",
    type=["csv"],
    help="Upload the 50-row synthetic urban grievance dataset."
)


# ============================================================
# STOP IF NO DATA
# ============================================================

if uploaded_file is None:

    st.warning(
        "Please upload the synthetic Dataset.csv file to view the dashboard."
    )

    st.divider()

    st.header("🧠 How the system works")

    workflow_preview = pd.DataFrame(
        {
            "Stage": [
                "Dataset",
                "Information Extraction",
                "Classification",
                "Grouping",
                "Pattern Detection",
                "Root-Cause Analysis",
                "Insight Report",
                "Human Verification"
            ],
            "Purpose": [
                "Collect complaint records",
                "Extract useful information",
                "Identify complaint categories",
                "Group similar complaints",
                "Detect recurring patterns",
                "Suggest possible contributing factors",
                "Create structured findings",
                "Validate findings using real-world evidence"
            ]
        }
    )

    st.dataframe(
        workflow_preview,
        use_container_width=True,
        hide_index=True
    )

    st.stop()


# ============================================================
# LOAD DATASET
# ============================================================

try:
    df = pd.read_csv(uploaded_file)

except Exception as e:

    st.error(f"Unable to read the CSV file: {e}")
    st.stop()


# ============================================================
# DATA VALIDATION
# ============================================================

required_columns = [
    "ID",
    "Complaint_Text",
    "Area",
    "Date",
    "Category",
    "Context"
]

missing_columns = [
    column for column in required_columns
    if column not in df.columns
]

if missing_columns:

    st.error(
        "The uploaded dataset is missing these required columns: "
        + ", ".join(missing_columns)
    )

    st.stop()


st.success(
    f"Dataset loaded successfully — {len(df)} complaint records detected."
)


# ============================================================
# EXECUTIVE DASHBOARD
# ============================================================

st.header("📊 Executive Dashboard")

total_complaints = len(df)
total_categories = df["Category"].nunique()
total_patterns = len(patterns_df)
total_fields = len(df.columns)

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.metric(
        "Total Complaints",
        total_complaints
    )

with m2:
    st.metric(
        "Categories",
        total_categories
    )

with m3:
    st.metric(
        "Verified Patterns",
        total_patterns
    )

with m4:
    st.metric(
        "Dataset Fields",
        total_fields
    )


st.caption(
    "Dashboard values are calculated from the uploaded synthetic dataset "
    "and the verified project analysis."
)


# ============================================================
# MAIN DASHBOARD TABS
# ============================================================

tab_overview, tab_dataset, tab_patterns, tab_factors, tab_report = st.tabs(
    [
        "📊 Overview",
        "🗂️ Dataset",
        "🔎 Pattern Analysis",
        "🧩 Root-Cause Analysis",
        "📋 Insight Report"
    ]
)


# ============================================================
# TAB 1 — OVERVIEW
# ============================================================

with tab_overview:

    st.header("📊 Complaint Overview")

    st.write(
        "Distribution of reported complaints across the seven categories "
        "present in the synthetic dataset."
    )

    category_counts = (
        df["Category"]
        .value_counts()
        .rename_axis("Category")
        .reset_index(name="Complaints")
    )

    chart_col, table_col = st.columns(
        [1.8, 1]
    )

    with chart_col:

        st.subheader("Complaint Categories")

        category_chart = category_counts.set_index("Category")

        st.bar_chart(
            category_chart["Complaints"],
            horizontal=True,
            height=380
        )

    with table_col:

        st.subheader("Category Summary")

        st.dataframe(
            category_counts,
            use_container_width=True,
            hide_index=True,
            height=380,
            column_config={
                "Category": st.column_config.TextColumn(
                    "Category"
                ),
                "Complaints": st.column_config.NumberColumn(
                    "Complaints",
                    format="%d"
                )
            }
        )

    st.divider()

    st.subheader("📌 Dataset Snapshot")

    snapshot1, snapshot2, snapshot3 = st.columns(3)

    with snapshot1:
        st.metric(
            "Most Reported Category",
            category_counts.iloc[0]["Category"]
        )

    with snapshot2:
        st.metric(
            "Highest Category Count",
            int(category_counts.iloc[0]["Complaints"])
        )

    with snapshot3:
        st.metric(
            "Records Used",
            total_complaints
        )

    st.info(
        "Complaint frequency represents reported complaints in the "
        "synthetic dataset. Frequency alone does not prove actual severity "
        "or physical cause."
    )


# ============================================================
# TAB 2 — DATASET
# ============================================================

with tab_dataset:

    st.header("🗂️ Dataset Explorer")

    st.write(
        "Explore the synthetic complaint records used by the analysis."
    )

    dataset_info1, dataset_info2, dataset_info3 = st.columns(3)

    with dataset_info1:
        st.metric("Rows", len(df))

    with dataset_info2:
        st.metric("Columns", len(df.columns))

    with dataset_info3:
        st.metric(
            "Unique Complaint IDs",
            df["ID"].nunique()
        )

    st.divider()

    st.subheader("Uploaded Records")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        height=500,
        column_config={
            "ID": st.column_config.TextColumn(
                "ID",
                width="small"
            ),
            "Complaint_Text": st.column_config.TextColumn(
                "Complaint",
                width="large"
            ),
            "Area": st.column_config.TextColumn(
                "Area",
                width="medium"
            ),
            "Date": st.column_config.TextColumn(
                "Date",
                width="small"
            ),
            "Category": st.column_config.TextColumn(
                "Category",
                width="medium"
            ),
            "Context": st.column_config.TextColumn(
                "Context",
                width="medium"
            )
        }
    )

    st.divider()

    st.subheader("🔍 Dataset Structure")

    structure_df = pd.DataFrame(
        {
            "Field": df.columns,
            "Purpose": [
                "Unique complaint identifier",
                "Original complaint description",
                "Reported area/location",
                "Complaint date",
                "Complaint category",
                "Additional contextual information"
            ]
        }
    )

    st.dataframe(
        structure_df,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# TAB 3 — PATTERN ANALYSIS
# ============================================================

with tab_patterns:

    st.header("🔎 Pattern & Hotspot Analysis")

    st.write(
        "Verified complaint groupings created from the synthetic dataset."
    )

    st.info(
        "The patterns below represent recurring complaint groupings. "
        "They should be interpreted as reported patterns, not confirmed "
        "real-world conditions."
    )

    st.subheader("Verified Complaint Patterns")

    st.dataframe(
        patterns_df,
        use_container_width=True,
        hide_index=True,
        height=510,
        column_config={
            "Pattern": st.column_config.TextColumn(
                "Pattern",
                width="medium"
            ),
            "Complaint Count": st.column_config.NumberColumn(
                "Complaint Count",
                format="%d",
                width="small"
            ),
            "Evidence IDs": st.column_config.TextColumn(
                "Evidence IDs",
                width="large"
            )
        }
    )

    st.divider()

    st.subheader("📈 Pattern Frequency")

    pattern_chart_df = (
        patterns_df[
            ["Pattern", "Complaint Count"]
        ]
        .sort_values(
            "Complaint Count",
            ascending=True
        )
        .set_index("Pattern")
    )

    st.bar_chart(
        pattern_chart_df["Complaint Count"],
        horizontal=True,
        height=500
    )

    st.caption(
        "Pattern frequency represents reported complaints in the "
        "synthetic dataset. It does not prove actual severity or cause."
    )

    st.divider()

    st.subheader("🧾 Evidence Reference")

    st.write(
        "Each pattern is connected to the complaint IDs that support "
        "the grouping."
    )

    evidence_view = patterns_df[
        [
            "Pattern",
            "Complaint Count",
            "Evidence IDs"
        ]
    ].copy()

    st.dataframe(
        evidence_view,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# TAB 4 — ROOT-CAUSE ANALYSIS
# ============================================================

with tab_factors:

    st.header("🧩 Possible Contributing Factors")

    st.write(
        "AI-assisted analysis suggests possible factors that could be "
        "investigated. These are hypotheses, not confirmed causes."
    )

    st.warning(
        "⚠️ Possible contributing factors must be checked against "
        "real-world evidence before any conclusion or action."
    )

    st.dataframe(
        factors_df,
        use_container_width=True,
        hide_index=True,
        height=520,
        column_config={
            "Pattern": st.column_config.TextColumn(
                "Pattern",
                width="medium"
            ),
            "Possible Contributing Factors": st.column_config.TextColumn(
                "Possible Contributing Factors",
                width="large"
            ),
            "Evidence Strength": st.column_config.TextColumn(
                "Evidence Strength",
                width="small"
            )
        }
    )

    st.divider()

    st.subheader("👤 Human Verification")

    st.info(
        "AI-generated contributing factors are hypotheses only. "
        "They must be checked against real-world evidence."
    )

    verification_items = [
        "Check relevant infrastructure and physical conditions.",
        "Check maintenance and service records where available.",
        "Verify reported blockages, damage, or service issues.",
        "Compare AI suggestions with real-world observations.",
        "Do not treat possible factors as confirmed causes."
    ]

    for item in verification_items:
        st.markdown(f"✓ {item}")

    st.divider()

    st.subheader("🧠 Responsible Interpretation")

    interpretation1, interpretation2 = st.columns(2)

    with interpretation1:

        with st.container(border=True):

            st.markdown("### Observed Evidence")

            st.write(
                "Information directly represented by complaint records "
                "and verified complaint groupings."
            )

    with interpretation2:

        with st.container(border=True):

            st.markdown("### AI Interpretation")

            st.write(
                "Possible contributing factors generated from observed "
                "patterns and requiring human verification."
            )


# ============================================================
# TAB 5 — INSIGHT & ACTION REPORT
# ============================================================

with tab_report:

    st.header("📋 Insight & Action Report")

    st.write(
        "A structured summary connecting observed complaint patterns, "
        "possible contributing factors, and recommended investigation."
    )

    st.info(
        "Human officials should review the findings based on real-world "
        "evidence, community impact, available resources, and relevant "
        "local conditions before deciding on any action."
    )

    st.dataframe(
        insight_df,
        use_container_width=True,
        hide_index=True,
        height=620,
        column_config={
            "Issue": st.column_config.TextColumn(
                "Issue",
                width="small"
            ),
            "Location": st.column_config.TextColumn(
                "Location",
                width="medium"
            ),
            "Complaint Count": st.column_config.NumberColumn(
                "Complaint Count",
                format="%d",
                width="small"
            ),
            "Observed Evidence": st.column_config.TextColumn(
                "Observed Evidence",
                width="large"
            ),
            "Possible Contributing Factor": st.column_config.TextColumn(
                "Possible Contributing Factor",
                width="large"
            ),
            "Recommended Investigation": st.column_config.TextColumn(
                "Recommended Investigation",
                width="large"
            ),
            "Important Limitation": st.column_config.TextColumn(
                "Important Limitation",
                width="large"
            )
        }
    )

    st.divider()

    st.subheader("⬇️ Export Report")

    report_csv = insight_df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        label="⬇️ Download Insight & Action Report",
        data=report_csv,
        file_name="SmartCity_Insight_Action_Report.csv",
        mime="text/csv"
    )

    st.caption(
        "The exported report contains the current verified analysis "
        "summary and associated limitations."
    )


# ============================================================
# OVERALL SUMMARY
# ============================================================

st.divider()

st.header("🧠 Overall Summary")

summary_col1, summary_col2 = st.columns(2)

with summary_col1:

    with st.container(border=True):

        st.subheader("What the AI found")

        st.markdown(
            """
            - Recurring urban complaint patterns
            - Repeated reports across specific locations
            - Complaint categories and frequencies
            - Possible contributing factors for investigation
            - Evidence IDs connecting patterns to source complaints
            """
        )

with summary_col2:

    with st.container(border=True):

        st.subheader("What the AI does NOT claim")

        st.markdown(
            """
            - It does not prove physical causes
            - It does not establish actual severity
            - It does not replace human investigation
            - It does not make government decisions
            - Synthetic complaint frequency is not the same as real-world impact
            """
        )


# ============================================================
# AI WORKFLOW
# ============================================================

st.divider()

st.header("🔄 AI Analysis Workflow")

workflow_df = pd.DataFrame(
    {
        "Stage": [
            "1. Dataset",
            "2. Information Extraction",
            "3. Complaint Classification",
            "4. Similar Grouping",
            "5. Pattern Detection",
            "6. Root-Cause Analysis",
            "7. Insight & Action Report",
            "8. Human Verification"
        ],
        "Purpose": [
            "Synthetic urban grievance records",
            "Extract structured information from complaints",
            "Assign complaint categories",
            "Group similar complaints",
            "Identify recurring patterns and locations",
            "Suggest possible contributing factors",
            "Create a structured investigation report",
            "Validate findings using real-world evidence"
        ]
    }
)

st.dataframe(
    workflow_df,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Stage": st.column_config.TextColumn(
            "Stage",
            width="medium"
        ),
        "Purpose": st.column_config.TextColumn(
            "Purpose",
            width="large"
        )
    }
)


# ============================================================
# SUSTAINABILITY CONTEXT
# ============================================================

st.divider()

st.header("🌱 Sustainability Context")

sdg_col, responsible_col = st.columns(2)

with sdg_col:

    with st.container(border=True):

        st.subheader("🌍 SDG 11 — Sustainable Cities and Communities")

        st.write(
            "The project explores how AI-assisted analysis can identify "
            "recurring urban grievance patterns and support further "
            "investigation."
        )

with responsible_col:

    with st.container(border=True):

        st.subheader("🤖 Responsible AI")

        st.markdown(
            """
            - Synthetic demonstration data
            - No real citizen PII
            - Possible factors clearly labelled
            - Human verification required
            - AI does not make government decisions
            """
        )


# ============================================================
# PROJECT LIMITATIONS
# ============================================================

st.divider()

with st.expander("⚠️ Important Project Limitations"):

    st.markdown(
        """
        **1. Synthetic dataset**

        This prototype uses demonstration data rather than live citizen
        complaint data.

        **2. Complaint reporting bias**

        Complaint volume reflects reported complaints and may not represent
        actual severity or the complete situation.

        **3. Possible causes are not confirmed causes**

        AI-generated contributing factors are hypotheses that require
        independent verification.

        **4. Human-in-the-loop**

        Real-world decisions should be made only after appropriate human
        review and verification.

        **5. No automated government decision-making**

        The system is designed as an analysis and decision-support
        prototype.
        """
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "🏙️ SmartCity Insight AI"
)

st.caption(
    "AI for Sustainability • SDG 11 • 1M1B Virtual Internship"
)

st.caption(
    "Synthetic demonstration prototype • Human-in-the-loop analysis"
)