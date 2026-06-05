import streamlit as st
import pandas as pd
import plotly.express as px
import io

st.set_page_config(page_title="DataStudio", layout="wide", page_icon="📊")

st.markdown("""
<style>
    .main { background-color: #0a0a0f; }
    .stApp { background-color: #0a0a0f; color: #f0f0ff; }
</style>
""", unsafe_allow_html=True)

st.title("📊 DataStudio — No-Code Data Intelligence")
st.markdown("---")

# ── DATA INPUT ──
st.sidebar.header("📥 Upload Your Data")
uploaded = st.sidebar.file_uploader("Upload CSV or Excel", type=["csv", "xlsx", "xls"])
paste = st.sidebar.text_area("Or paste CSV data here:", height=200)
st.sidebar.markdown("---")

df = None

if uploaded:
    try:
        if uploaded.name.endswith(".csv"):
            df = pd.read_csv(uploaded)
        else:
            df = pd.read_excel(uploaded)
        st.sidebar.success(f"✅ Loaded: {uploaded.name}")
    except Exception as e:
        st.sidebar.error(f"Error: {e}")

elif paste.strip():
    try:
        df = pd.read_csv(io.StringIO(paste))
        st.sidebar.success("✅ Data loaded from text!")
    except Exception as e:
        st.sidebar.error(f"Could not parse: {e}")

# ── TABS ──
if df is not None:
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Overview", "🧹 Clean", "📈 Visualize", "🔍 Extract"])

    # ── OVERVIEW ──
    with tab1:
        st.subheader("Data Overview")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Rows", df.shape[0])
        c2.metric("Columns", df.shape[1])
        c3.metric("Missing Values", int(df.isnull().sum().sum()))
        c4.metric("Numeric Columns", len(df.select_dtypes(include='number').columns))
        st.markdown("### Data Preview")
        st.dataframe(df, use_container_width=True)

    # ── CLEAN ──
    with tab2:
        st.subheader("Data Cleaning")
        clean_df = df.copy()

        missing = df.isnull().sum()
        missing = missing[missing > 0]

        if len(missing) > 0:
            st.markdown("### Missing Values")
            st.dataframe(missing.rename("Missing Count"), use_container_width=True)

            if st.button("Fill Missing (numeric=mean, text=Unknown)"):
                for col in clean_df.columns:
                    if clean_df[col].dtype in ['float64','int64']:
                        clean_df[col].fillna(clean_df[col].mean(), inplace=True)
                    else:
                        clean_df[col].fillna("Unknown", inplace=True)
                st.success("✅ Missing values filled!")
                st.dataframe(clean_df, use_container_width=True)
        else:
            st.success("✅ No missing values found!")

        dups = df.duplicated().sum()
        st.markdown(f"### Duplicates: **{dups}** found")
        if dups > 0 and st.button("Remove Duplicates"):
            clean_df = clean_df.drop_duplicates()
            st.success(f"✅ Removed {dups} duplicate rows!")
            st.dataframe(clean_df, use_container_width=True)

        st.markdown("### Download Cleaned Data")
        csv = clean_df.to_csv(index=False).encode('utf-8')
        st.download_button("⬇️ Download Clean CSV", csv, "cleaned_data.csv", "text/csv")

    # ── VISUALIZE ──
    with tab3:
        st.subheader("Visualizations")
        num_cols = df.select_dtypes(include='number').columns.tolist()
        cat_cols = df.select_dtypes(exclude='number').columns.tolist()

        if num_cols:
            col1, col2 = st.columns(2)

            with col1:
                st.markdown("#### Distribution")
                sel = st.selectbox("Select numeric column", num_cols, key="dist")
                fig = px.histogram(df, x=sel, template="plotly_dark", color_discrete_sequence=["#7c6aff"])
                st.plotly_chart(fig, use_container_width=True)

            with col2:
                st.markdown("#### Box Plot")
                sel2 = st.selectbox("Select column", num_cols, key="box")
                fig2 = px.box(df, y=sel2, template="plotly_dark", color_discrete_sequence=["#ff6a6a"])
                st.plotly_chart(fig2, use_container_width=True)

            if len(num_cols) >= 2:
                st.markdown("#### Scatter Plot")
                c1, c2 = st.columns(2)
                x_col = c1.selectbox("X axis", num_cols, key="sx")
                y_col = c2.selectbox("Y axis", num_cols, index=1, key="sy")
                color_col = st.selectbox("Color by (optional)", ["None"] + cat_cols, key="sc")
                fig3 = px.scatter(df, x=x_col, y=y_col,
                                  color=None if color_col=="None" else color_col,
                                  template="plotly_dark")
                st.plotly_chart(fig3, use_container_width=True)

            if cat_cols:
                st.markdown("#### Bar Chart")
                cat = st.selectbox("Category column", cat_cols, key="bc")
                num = st.selectbox("Numeric column", num_cols, key="bn")
                fig4 = px.bar(df.groupby(cat)[num].mean().reset_index(),
                              x=cat, y=num, template="plotly_dark",
                              color_discrete_sequence=["#6affb0"])
                st.plotly_chart(fig4, use_container_width=True)
        else:
            st.info("No numeric columns found for visualization.")

    # ── EXTRACT ──
    with tab4:
        st.subheader("Data Extraction")

        st.markdown("### Column Info")
        info_df = pd.DataFrame({
            "Column": df.columns,
            "Type": df.dtypes.values,
            "Non-Null": df.notnull().sum().values,
            "Missing": df.isnull().sum().values,
            "Unique": df.nunique().values
        })
        st.dataframe(info_df, use_container_width=True)

        num_cols = df.select_dtypes(include='number').columns.tolist()
        if num_cols:
            st.markdown("### Numeric Statistics")
            st.dataframe(df[num_cols].describe(), use_container_width=True)

        cat_cols = df.select_dtypes(exclude='number').columns.tolist()
        if cat_cols:
            st.markdown("### Categorical Value Counts")
            sel = st.selectbox("Select column", cat_cols, key="vc")
            st.dataframe(df[sel].value_counts().reset_index(), use_container_width=True)

else:
    st.info("👈 Upload a file or paste CSV data in the sidebar to get started!")
    st.markdown("""
    ### How to use:
    1. **Upload** a CSV/Excel file using the sidebar, or **paste** CSV text directly
    2. Explore the **Overview** tab to see your data
    3. Use the **Clean** tab to fix missing values and duplicates
    4. Go to **Visualize** for interactive charts
    5. Check **Extract** for detailed statistics
    """)
