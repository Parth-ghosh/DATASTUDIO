import streamlit as st
import pandas as pd
import plotly.express as px
import io

st.set_page_config(page_title="DataStudio", layout="wide", page_icon="📊")

if 'show_cover' not in st.session_state:
    st.session_state.show_cover = True

st.markdown("""<style>
html,body,[data-testid="stAppViewContainer"],[data-testid="stMain"]{background:#0a0a0f!important;color:#f0f0ff!important}
[data-testid="stSidebar"]{background:#111118!important;border-right:1px solid rgba(255,255,255,0.08)}
[data-testid="stSidebar"] *{color:#f0f0ff!important}
.stButton>button{background:linear-gradient(135deg,#7c6aff,#a78bfa)!important;color:white!important;border:none!important;border-radius:12px!important;font-weight:700!important;font-size:15px!important;box-shadow:0 4px 20px rgba(124,106,255,0.35)!important}
.stTabs [data-baseweb="tab-list"]{background:#111118!important;border-bottom:1px solid rgba(255,255,255,0.08)!important}
.stTabs [data-baseweb="tab"]{background:transparent!important;color:rgba(240,240,255,0.5)!important;font-size:14px!important;font-weight:500!important;padding:14px 22px!important}
.stTabs [aria-selected="true"]{background:transparent!important;color:#f0f0ff!important;border-bottom:2px solid #7c6aff!important}
.stTabs [data-baseweb="tab-panel"]{background:#0a0a0f!important;padding:24px 0!important}
[data-testid="stMetric"]{background:#111118!important;border:1px solid rgba(255,255,255,0.08)!important;border-radius:16px!important;padding:20px!important}
[data-testid="stMetricValue"]{color:#f0f0ff!important;font-size:32px!important;font-weight:800!important}
[data-testid="stTextArea"] textarea{background:#1a1a24!important;color:#f0f0ff!important;border:1px solid rgba(255,255,255,0.08)!important;border-radius:12px!important;font-family:monospace!important}
h1,h2,h3,h4{color:#f0f0ff!important}
p,li{color:rgba(240,240,255,0.7)!important}
@keyframes fadeUp{from{opacity:0;transform:translateY(40px)}to{opacity:1;transform:translateY(0)}}
@keyframes floatA{0%,100%{transform:translateY(0) rotate(0deg)}50%{transform:translateY(-30px) rotate(5deg)}}
@keyframes floatB{0%,100%{transform:translateY(0)}50%{transform:translateY(-20px)}}
@keyframes spinSlow{from{transform:rotate(0deg)}to{transform:rotate(360deg)}}
@keyframes gradShift{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
@keyframes pulse{0%,100%{box-shadow:0 0 40px rgba(124,106,255,0.4)}50%{box-shadow:0 0 80px rgba(124,106,255,0.8)}}
</style>""", unsafe_allow_html=True)

if st.session_state.show_cover:
    st.markdown("""
<div style="position:relative;width:100%;min-height:95vh;background:radial-gradient(ellipse at 20% 20%,rgba(124,106,255,0.15) 0%,transparent 60%),radial-gradient(ellipse at 80% 80%,rgba(255,106,106,0.1) 0%,transparent 60%),#0a0a0f;display:flex;flex-direction:column;align-items:center;justify-content:center;overflow:hidden;padding:60px 20px;border-radius:16px;">
<div style="position:absolute;inset:0;background-image:linear-gradient(rgba(124,106,255,0.06) 1px,transparent 1px),linear-gradient(90deg,rgba(124,106,255,0.06) 1px,transparent 1px);background-size:60px 60px;"></div>
<div style="position:absolute;top:8%;left:6%;width:120px;height:120px;border-radius:50%;background:linear-gradient(135deg,rgba(124,106,255,0.35),rgba(167,139,250,0.2));filter:blur(2px);animation:floatA 7s ease-in-out infinite;border:1px solid rgba(124,106,255,0.3);"></div>
<div style="position:absolute;top:15%;right:8%;width:80px;height:80px;background:linear-gradient(135deg,rgba(255,106,106,0.3),rgba(255,154,154,0.15));filter:blur(1px);animation:floatB 9s ease-in-out infinite 1s;transform:rotate(45deg);border:1px solid rgba(255,106,106,0.3);border-radius:12px;"></div>
<div style="position:absolute;bottom:20%;left:5%;width:100px;height:100px;background:linear-gradient(135deg,rgba(106,255,176,0.25),rgba(160,255,207,0.1));filter:blur(1px);animation:floatA 8s ease-in-out infinite 2s;border:1px solid rgba(106,255,176,0.25);border-radius:8px;transform:rotate(15deg);"></div>
<div style="position:absolute;bottom:25%;right:6%;width:90px;height:90px;border-radius:50%;background:linear-gradient(135deg,rgba(255,202,106,0.25),rgba(255,202,106,0.1));filter:blur(1px);animation:floatB 10s ease-in-out infinite 3s;border:1px solid rgba(255,202,106,0.25);"></div>
<div style="position:absolute;top:-150px;left:-150px;width:500px;height:500px;border-radius:50%;background:rgba(124,106,255,0.08);filter:blur(80px);pointer-events:none;"></div>
<div style="position:absolute;bottom:-100px;right:-100px;width:400px;height:400px;border-radius:50%;background:rgba(255,106,106,0.06);filter:blur(80px);pointer-events:none;"></div>
<div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:600px;height:600px;border-radius:50%;border:1px dashed rgba(124,106,255,0.1);pointer-events:none;animation:spinSlow 30s linear infinite;"></div>
<div style="position:relative;z-index:10;text-align:center;max-width:700px;">
<div style="width:100px;height:100px;margin:0 auto 32px;background:linear-gradient(135deg,rgba(124,106,255,0.2),rgba(255,106,106,0.1));border:1px solid rgba(124,106,255,0.35);border-radius:24px;display:flex;align-items:center;justify-content:center;font-size:48px;box-shadow:0 8px 40px rgba(124,106,255,0.25);animation:fadeUp 0.8s ease 0.2s both;">📊</div>
<div style="display:inline-block;background:rgba(124,106,255,0.12);border:1px solid rgba(124,106,255,0.35);color:#a78bfa;font-size:11px;letter-spacing:3px;padding:6px 20px;border-radius:100px;margin-bottom:24px;animation:fadeUp 0.8s ease 0.4s both;font-family:monospace;">✦ NO-CODE DATA INTELLIGENCE ✦</div>
<div style="font-size:clamp(56px,9vw,100px);font-weight:900;line-height:0.95;letter-spacing:-3px;margin-bottom:8px;animation:fadeUp 0.8s ease 0.6s both;"><span style="color:#f0f0ff;">Data</span><span style="background:linear-gradient(135deg,#7c6aff 0%,#a78bfa 40%,#ff6a6a 80%);background-size:200% 200%;-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;animation:gradShift 4s ease infinite;">Studio</span></div>
<p style="font-size:20px;color:rgba(240,240,255,0.6);margin:20px auto 0;max-width:480px;line-height:1.6;animation:fadeUp 0.8s ease 0.8s both;">Drop your data. Watch the magic happen.<br>Clean, analyze, extract, visualize — zero code.</p>
<div style="display:flex;gap:40px;justify-content:center;margin-top:40px;animation:fadeUp 0.8s ease 1s both;">
<div style="text-align:center;"><div style="font-size:28px;font-weight:800;color:#7c6aff;">4</div><div style="font-size:12px;color:rgba(240,240,255,0.4);font-family:monospace;letter-spacing:1px;">TABS</div></div>
<div style="width:1px;background:rgba(255,255,255,0.08);"></div>
<div style="text-align:center;"><div style="font-size:28px;font-weight:800;color:#ff6a6a;">∞</div><div style="font-size:12px;color:rgba(240,240,255,0.4);font-family:monospace;letter-spacing:1px;">ROWS</div></div>
<div style="width:1px;background:rgba(255,255,255,0.08);"></div>
<div style="text-align:center;"><div style="font-size:28px;font-weight:800;color:#6affb0;">0</div><div style="font-size:12px;color:rgba(240,240,255,0.4);font-family:monospace;letter-spacing:1px;">CODE</div></div>
</div>
<div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-top:36px;animation:fadeUp 0.8s ease 1.2s both;">
<div style="display:flex;align-items:center;gap:8px;background:rgba(124,106,255,0.08);border:1px solid rgba(124,106,255,0.2);padding:8px 16px;border-radius:100px;"><div style="width:8px;height:8px;border-radius:50%;background:#7c6aff;"></div><span style="font-size:13px;color:rgba(240,240,255,0.7);">Instant Clean</span></div>
<div style="display:flex;align-items:center;gap:8px;background:rgba(255,106,106,0.08);border:1px solid rgba(255,106,106,0.2);padding:8px 16px;border-radius:100px;"><div style="width:8px;height:8px;border-radius:50%;background:#ff6a6a;"></div><span style="font-size:13px;color:rgba(240,240,255,0.7);">Smart Analyze</span></div>
<div style="display:flex;align-items:center;gap:8px;background:rgba(106,255,176,0.08);border:1px solid rgba(106,255,176,0.2);padding:8px 16px;border-radius:100px;"><div style="width:8px;height:8px;border-radius:50%;background:#6affb0;"></div><span style="font-size:13px;color:rgba(240,240,255,0.7);">Auto Extract</span></div>
<div style="display:flex;align-items:center;gap:8px;background:rgba(255,202,106,0.08);border:1px solid rgba(255,202,106,0.2);padding:8px 16px;border-radius:100px;"><div style="width:8px;height:8px;border-radius:50%;background:#ffca6a;"></div><span style="font-size:13px;color:rgba(240,240,255,0.7);">Rich Visualize</span></div>
</div>
</div>
</div>
""", unsafe_allow_html=True)
    col1,col2,col3 = st.columns([2,1,2])
    with col2:
        if st.button("🚀  Get Started", use_container_width=True):
            st.session_state.show_cover = False
            st.rerun()

else:
    st.markdown("""<div style="display:flex;align-items:center;gap:14px;padding:8px 0 24px;border-bottom:1px solid rgba(255,255,255,0.08);margin-bottom:28px;">
<div style="font-size:32px;">📊</div>
<div><div style="font-size:22px;font-weight:800;color:#f0f0ff;">DataStudio</div>
<div style="font-size:12px;color:rgba(240,240,255,0.4);font-family:monospace;letter-spacing:2px;">NO-CODE DATA INTELLIGENCE</div></div>
</div>""", unsafe_allow_html=True)

    st.sidebar.markdown("""<div style="padding:8px 0 20px;border-bottom:1px solid rgba(255,255,255,0.08);margin-bottom:20px;">
<div style="font-size:11px;letter-spacing:2px;text-transform:uppercase;color:rgba(240,240,255,0.4);font-family:monospace;">Data Input</div>
<div style="font-size:16px;font-weight:700;">📥 Load Your Data</div></div>""", unsafe_allow_html=True)

    uploaded = st.sidebar.file_uploader("Upload CSV or Excel", type=["csv","xlsx","xls"])
    st.sidebar.markdown("<div style='margin:10px 0;text-align:center;color:rgba(240,240,255,0.3);font-size:12px;'>— or —</div>", unsafe_allow_html=True)
    paste = st.sidebar.text_area("Paste CSV data:", height=160, placeholder="Name,Age,City\nAlice,28,New York")
    if st.sidebar.button("↩ Back to Cover"):
        st.session_state.show_cover = True
        st.rerun()

    df = None
    if uploaded:
        try:
            df = pd.read_csv(uploaded) if uploaded.name.endswith(".csv") else pd.read_excel(uploaded)
            st.sidebar.success(f"✅ {uploaded.name} — {df.shape[0]}r × {df.shape[1]}c")
        except Exception as e:
            st.sidebar.error(str(e))
    elif paste.strip():
        try:
            df = pd.read_csv(io.StringIO(paste))
            st.sidebar.success(f"✅ {df.shape[0]} rows × {df.shape[1]} cols")
        except Exception as e:
            st.sidebar.error(str(e))

    if df is not None:
        tab1,tab2,tab3,tab4 = st.tabs(["📊  Overview","🧹  Clean","📈  Visualize","🔍  Extract"])

        with tab1:
            st.markdown("### Data Overview")
            c1,c2,c3,c4 = st.columns(4)
            c1.metric("🗂 Rows", df.shape[0])
            c2.metric("📋 Columns", df.shape[1])
            c3.metric("⚠️ Missing", int(df.isnull().sum().sum()))
            c4.metric("🔢 Numeric", len(df.select_dtypes(include='number').columns))
            st.markdown("#### Data Preview")
            st.dataframe(df, use_container_width=True, height=380)
            c1,c2 = st.columns(2)
            c1.download_button("⬇️ Download CSV", df.to_csv(index=False).encode(), "data.csv", "text/csv", use_container_width=True)
            c2.download_button("⬇️ Download JSON", df.to_json(orient='records',indent=2).encode(), "data.json", use_container_width=True)

        with tab2:
            st.markdown("### Data Cleaning")
            clean_df = df.copy()
            c1,c2 = st.columns(2)
            with c1:
                st.markdown("#### 🕳️ Missing Values")
                missing = df.isnull().sum()
                missing = missing[missing>0]
                if len(missing)>0:
                    st.dataframe(missing.rename("Missing Count"), use_container_width=True)
                    if st.button("✨ Fill Missing Values", use_container_width=True):
                        for col in clean_df.columns:
                            if clean_df[col].dtype in ['float64','int64']:
                                clean_df[col].fillna(clean_df[col].mean(), inplace=True)
                            else:
                                clean_df[col].fillna("Unknown", inplace=True)
                        st.success("✅ Filled! numeric→mean, text→Unknown")
                        st.dataframe(clean_df, use_container_width=True)
                else:
                    st.success("✅ No missing values!")
            with c2:
                st.markdown("#### 👥 Duplicates")
                dups = df.duplicated().sum()
                st.markdown(f"<div style='background:rgba(255,106,106,0.1);border:1px solid rgba(255,106,106,0.3);border-radius:12px;padding:16px;text-align:center;margin-bottom:16px;'><div style='font-size:32px;font-weight:800;color:#ff6a6a;'>{dups}</div><div style='font-size:13px;color:rgba(240,240,255,0.5);'>duplicate rows</div></div>", unsafe_allow_html=True)
                if dups>0 and st.button("🗑️ Remove Duplicates", use_container_width=True):
                    clean_df = clean_df.drop_duplicates()
                    st.success(f"✅ Removed {dups} rows!")
                    st.dataframe(clean_df, use_container_width=True)
                elif dups==0:
                    st.success("✅ No duplicates!")
            st.download_button("⬇️ Download Cleaned CSV", clean_df.to_csv(index=False).encode(), "cleaned.csv", use_container_width=True)

        with tab3:
            st.markdown("### Visualizations")
            num_cols = df.select_dtypes(include='number').columns.tolist()
            cat_cols = df.select_dtypes(exclude='number').columns.tolist()
            dark = dict(paper_bgcolor='#111118',plot_bgcolor='#111118',font_color='rgba(240,240,255,0.7)',title_font_color='#f0f0ff')
            if num_cols:
                c1,c2 = st.columns(2)
                with c1:
                    sel = st.selectbox("Distribution column", num_cols, key="d")
                    fig = px.histogram(df,x=sel,template="plotly_dark",color_discrete_sequence=["#7c6aff"],title=f"Distribution — {sel}")
                    fig.update_layout(**dark); st.plotly_chart(fig,use_container_width=True)
                with c2:
                    sel2 = st.selectbox("Box plot column", num_cols, key="b")
                    fig2 = px.box(df,y=sel2,template="plotly_dark",color_discrete_sequence=["#ff6a6a"],title=f"Box Plot — {sel2}")
                    fig2.update_layout(**dark); st.plotly_chart(fig2,use_container_width=True)
                if len(num_cols)>=2:
                    c1,c2,c3 = st.columns(3)
                    xc=c1.selectbox("X",num_cols,key="sx"); yc=c2.selectbox("Y",num_cols,index=1,key="sy"); cc=c3.selectbox("Color",["None"]+cat_cols,key="sc")
                    fig3=px.scatter(df,x=xc,y=yc,color=None if cc=="None" else cc,template="plotly_dark",title=f"{xc} vs {yc}",color_discrete_sequence=["#7c6aff","#ff6a6a","#6affb0"])
                    fig3.update_layout(**dark); st.plotly_chart(fig3,use_container_width=True)
                if cat_cols:
                    c1,c2=st.columns(2)
                    with c1:
                        cat=st.selectbox("Bar category",cat_cols,key="bc"); num=st.selectbox("Bar numeric",num_cols,key="bn")
                        fig4=px.bar(df.groupby(cat)[num].mean().reset_index(),x=cat,y=num,template="plotly_dark",color_discrete_sequence=["#6affb0"],title=f"Avg {num} by {cat}")
                        fig4.update_layout(**dark); st.plotly_chart(fig4,use_container_width=True)
                    with c2:
                        cat2=st.selectbox("Pie column",cat_cols,key="pc")
                        fig5=px.pie(df,names=cat2,template="plotly_dark",color_discrete_sequence=["#7c6aff","#ff6a6a","#6affb0","#ffca6a"],title=f"{cat2} Distribution")
                        fig5.update_layout(**dark); st.plotly_chart(fig5,use_container_width=True)

        with tab4:
            st.markdown("### Data Extraction")
            c1,c2=st.columns(2)
            with c1:
                st.markdown("#### 📋 Column Summary")
                st.dataframe(pd.DataFrame({"Column":df.columns,"Type":df.dtypes.astype(str).values,"Non-Null":df.notnull().sum().values,"Missing":df.isnull().sum().values,"Unique":df.nunique().values}),use_container_width=True,hide_index=True)
            with c2:
                num_cols=df.select_dtypes(include='number').columns.tolist()
                if num_cols:
                    st.markdown("#### 📐 Statistics")
                    st.dataframe(df[num_cols].describe().round(2),use_container_width=True)
            cat_cols=df.select_dtypes(exclude='number').columns.tolist()
            if cat_cols:
                st.markdown("#### 🏷️ Value Counts")
                sel=st.selectbox("Column",cat_cols,key="vc")
                vc=df[sel].value_counts().reset_index(); vc.columns=[sel,"Count"]
                c1,c2=st.columns([1,2])
                with c1: st.dataframe(vc,use_container_width=True,hide_index=True)
                with c2:
                    dark = dict(paper_bgcolor='#111118',plot_bgcolor='#111118',font_color='rgba(240,240,255,0.7)',title_font_color='#f0f0ff')
                    fig=px.bar(vc.head(15),x=sel,y="Count",template="plotly_dark",color_discrete_sequence=["#7c6aff"],title=f"Top values in '{sel}'")
                    fig.update_layout(**dark); st.plotly_chart(fig,use_container_width=True)
    else:
        st.markdown("""<div style="text-align:center;padding:80px 20px;">
<div style="font-size:64px;margin-bottom:24px;opacity:0.4;">📂</div>
<h2 style="color:rgba(240,240,255,0.5)!important;margin-bottom:12px;">No data loaded yet</h2>
<p style="color:rgba(240,240,255,0.3)!important;max-width:380px;margin:0 auto;">Upload a CSV/Excel file or paste CSV text in the sidebar to begin.</p>
</div>""", unsafe_allow_html=True)
