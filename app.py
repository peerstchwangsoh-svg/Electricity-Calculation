import streamlit as st
import streamlit.components.v1 as components

# 1. ตั้งค่าโครงสร้างหน้าเว็บให้ทันสมัย
st.set_page_config(
    page_title="Electrical Master App ⚡",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ⚡ เอฟเฟกต์สายฟ้าโปรยปรายเมื่อเปิดหน้าเว็บ
st.snow()

# ตกแต่ง CSS เพิ่มเติมเพื่อความสวยงามขั้นสุด
st.markdown(
    """
    <style>
    /* ตกแต่งสายฟ้าสีเหลือง */
    .snowflake { color: #ffd700 !important; font-size: 28px !important; }
    .snowflake::after { content: "⚡" !important; }
    
    /* สไตล์การ์ดข้อมูล */
    .metric-card {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        border: 2px solid #3b82f6;
        color: white;
        text-align: center;
        margin-bottom: 15px;
    }
    .metric-title {
        font-size: 1.1rem;
        color: #94a3b8;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .metric-value {
        font-size: 2.2rem;
        font-weight: 800;
        color: #60a5fa;
    }
    .metric-unit {
        font-size: 1rem;
        color: #38bdf8;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# เมนูหลักด้านข้าง
st.sidebar.markdown("# ⚙️ เมนูควบคุม")
menu = st.sidebar.selectbox(
    "เลือกฟังก์ชันการทำงาน",
    [
        "🏠 หน้าแรก & ทฤษฎี", 
        "🧮 เครื่องคำนวณกฎของโอห์ม (มีตัวแปลง Kilo/Milli)", 
        "💡 วงจรจำลองเสมือนจริง (Interactive Circuit)", 
        "📟 เครื่องวัดมัลติมิเตอร์", 
        "📝 แบบทดสอบเก็บคะแนน"
    ]
)

# ลิงก์รูปภาพที่ผ่านการตรวจสอบแล้ว
OHM_WHEEL_IMG = "http://googleusercontent.com/image_collection/image_retrieval/8355741260134288511_0"
MULTIMETER_IMG = "http://googleusercontent.com/image_collection/image_retrieval/11592891170833533756_0"

# ----------------- หน้า 1: หน้าแรก & ทฤษฎี -----------------
if menu == "🏠 หน้าแรก & ทฤษฎี":
    st.title("⚡ ยินดีต้อนรับสู่แอปพลิเคชันวัดและวิเคราะห์ไฟฟ้า")
    st.write("เครื่องมือช่วยเรียนรู้เรื่องไฟฟ้า คณนาสูตร และการวัดค่าอย่างแม่นยำ")
    st.write("---")
    
    col_left, col_right = st.columns([1.2, 1])
    
    with col_left:
        st.subheader("📖 ทฤษฎีพื้นฐานของกฎของโอห์ม (Ohm's Law)")
        st.write(
            "กฎของโอห์มระบุว่า **'กระแสไฟฟ้าที่ไหลผ่านตัวนำจะเป็นสัดส่วนโดยตรงกับแรงดันไฟฟ้า และเป็นสัดส่วนผกผันกับความต้านทาน'**"
        )
        st.latex(r"V = I \times R \quad \Rightarrow \quad I = \frac{V}{R} \quad \Rightarrow \quad R = \frac{V}{I}")
        
        st.info(
            "💡 **จำง่ายๆ ด้วยหลักสามเหลี่ยม:**\n"
            "- ปิดตัว **V** จะได้ **I x R**\n"
            "- ปิดตัว **I** จะได้ **V / R**\n"
            "- ปิดตัว **R** จะได้ **V / I**"
        )
        
        # แสดงสูตรเพิ่มเติมนอกจากกฎของโอห์มคือสูตรกำลังไฟฟ้า (Power)
        st.subheader("🔋 สูตรพลังงานและกำลังไฟฟ้า (Electrical Power)")
        st.latex(r"P = V \times I \quad \text{หรือ} \quad P = I^2 \times R \quad \text{หรือ} \quad P = \frac{V^2}{R}")
        st.write("โดยที่ **P** คือ กำลังไฟฟ้า มีหน่วยเป็น **วัตต์ (Watt - W)**")

    with col_right:
        st.subheader("📊 แผนผังสูตรกฎของโอห์ม (Ohm's Law Wheel)")
        st.image(OHM_WHEEL_IMG, caption="Ohm's Law & Power Formula Wheel (วงล้ออ้างอิงสูตรคำนวณทั้งหมด)", use_container_width=True)


# ----------------- หน้า 2: เครื่องคำนวณกฎของโอห์ม -----------------
elif menu == "🧮 เครื่องคำนวณกฎของโอห์ม (มีตัวแปลง Kilo/Milli)":
    st.title("🧮 เครื่องคำนวณกฎของโอห์มระดับสูง")
    st.write("สามารถเลือกและแปลงหน่วยพรีฟิกซ์ เช่น Kilo, Mega, Milli, Micro ได้ทันที!")
    st.write("---")

    calc_option = st.selectbox(
        "คุณต้องการคำนวณหาค่าอะไร?", 
        ["หา แรงดันไฟฟ้า (Voltage - V)", "หา กระแสไฟฟ้า (Current - I)", "หา ความต้านทาน (Resistance - R)"]
    )

    # ตัวคูณสำหรับแปลงหน่วยกลับเป็นค่ามาตรฐาน (Base unit)
    unit_multipliers = {
        "Micro (μ)": 1e-6,
        "Milli (m)": 1e-3,
        "หน่วยพื้นฐาน (Base)": 1.0,
        "Kilo (k)": 1e3,
        "Mega (M)": 1e6
    }

    st.markdown("### 📥 ป้อนค่าพารามิเตอร์ที่คุณทราบ")
    
    col1, col2 = st.columns(2)

    if calc_option == "หา แรงดันไฟฟ้า (Voltage - V)":
        with col1:
            i_val = st.number_input("ค่ากระแสไฟฟ้า (I)", min_value=0.0, value=1.0, format="%.6f")
            i_unit = st.selectbox("หน่วยของกระแสไฟฟ้า (I)", ["Micro (μ)", "Milli (m)", "หน่วยพื้นฐาน (Base)", "Kilo (k)"], index=2)
        with col2:
            r_val = st.number_input("ค่าความต้านทาน (R)", min_value=0.0, value=10.0, format="%.6f")
            r_unit = st.selectbox("หน่วยของความต้านทาน (R)", ["หน่วยพื้นฐาน (Base)", "Kilo (k)", "Mega (M)"], index=0)
            
        if st.button("🚀 คำนวณหาแรงดันไฟฟ้า (V)", use_container_width=True):
            st.snow()
            # แปลงค่าเข้าสู่หน่วยพื้นฐานก่อนคำนวณ
            i_base = i_val * unit_multipliers[i_unit]
            r_base = r_val * unit_multipliers[r_unit]
            v_base = i_base * r_base
            
            # แปลงผลลัพธ์กลับให้เป็นหน่วยต่างๆ เพื่อความสะดวกในการใช้งาน
            st.markdown("### 📊 ผลลัพธ์การคำนวณ")
            col_res1, col_res2, col_res3 = st.columns(3)
            with col_res1:
                st.markdown(f'<div class="metric-card"><div class="metric-title">แรงดันไฟฟ้า (mV)</div><div class="metric-value">{v_base*1e3:,.3f}</div><div class="metric-unit">มิลลิโวลต์ (mV)</div></div>', unsafe_allow_html=True)
            with col_res2:
                st.markdown(f'<div class="metric-card" style="border-color:#10b981;"><div class="metric-title">แรงดันไฟฟ้า (V)</div><div class="metric-value" style="color:#10b981;">{v_base:,.4f}</div><div class="metric-unit">โวลต์ (V)</div></div>', unsafe_allow_html=True)
            with col_res3:
                st.markdown(f'<div class="metric-card" style="border-color:#f59e0b;"><div class="metric-title">แรงดันไฟฟ้า (kV)</div><div class="metric-value" style="color:#f59e0b;">{v_base/1e3:,.6f}</div><div class="metric-unit">กิโลโวลต์ (kV)</div></div>', unsafe_allow_html=True)
            
            st.latex(rf"V = I \times R = ({i_val} \text{{ {i_unit.split()[0]}}}) \times ({r_val} \text{{ {r_unit.split()[0]}}}) = {v_base:,.4f} \text{{ V}}")

    elif calc_option == "หา กระแสไฟฟ้า (Current - I)":
        with col1:
            v_val = st.number_input("ค่าแรงดันไฟฟ้า (V)", min_value=0.0, value=220.0, format="%.6f")
            v_unit = st.selectbox("หน่วยของแรงดันไฟฟ้า (V)", ["Milli (m)", "หน่วยพื้นฐาน (Base)", "Kilo (k)"], index=1)
        with col2:
            r_val = st.number_input("ค่าความต้านทาน (R)", min_value=0.001, value=100.0, format="%.6f")
            r_unit = st.selectbox("หน่วยของความต้านทาน (R)", ["หน่วยพื้นฐาน (Base)", "Kilo (k)", "Mega (M)"], index=0)
            
        if st.button("🚀 คำนวณหากระแสไฟฟ้า (I)", use_container_width=True):
            st.snow()
            v_base = v_val * unit_multipliers[v_unit]
            r_base = r_val * unit_multipliers[r_unit]
            i_base = v_base / r_base
            
            st.markdown("### 📊 ผลลัพธ์การคำนวณ")
            col_res1, col_res2, col_res3 = st.columns(3)
            with col_res1:
                st.markdown(f'<div class="metric-card"><div class="metric-title">กระแสไฟฟ้า (μA)</div><div class="metric-value">{i_base*1e6:,.2f}</div><div class="metric-unit">ไมโครแอมแปร์ (μA)</div></div>', unsafe_allow_html=True)
            with col_res2:
                st.markdown(f'<div class="metric-card" style="border-color:#10b981;"><div class="metric-title">กระแสไฟฟ้า (mA)</div><div class="metric-value" style="color:#10b981;">{i_base*1000:,.3f}</div><div class="metric-unit">มิลลิแอมแปร์ (mA)</div></div>', unsafe_allow_html=True)
            with col_res3:
                st.markdown(f'<div class="metric-card" style="border-color:#e11d48;"><div class="metric-title">กระแสไฟฟ้า (A)</div><div class="metric-value" style="color:#e11d48;">{i_base:,.6f}</div><div class="metric-unit">แอมแปร์ (A)</div></div>', unsafe_allow_html=True)

            st.latex(rf"I = \frac{{V}}{{R}} = \frac{{{v_val} \text{{ {v_unit.split()[0]}}}}}{{{r_val} \text{{ {r_unit.split()[0]}}}}} = {i_base:,.6f} \text{{ A}}")

    elif calc_option == "หา ความต้านทาน (Resistance - R)":
        with col1:
            v_val = st.number_input("ค่าแรงดันไฟฟ้า (V)", min_value=0.0, value=12.0, format="%.6f")
            v_unit = st.selectbox("หน่วยของแรงดันไฟฟ้า (V)", ["Milli (m)", "หน่วยพื้นฐาน (Base)", "Kilo (k)"], index=1)
        with col2:
            i_val = st.number_input("ค่ากระแสไฟฟ้า (I)", min_value=0.000001, value=0.5, format="%.6f")
            i_unit = st.selectbox("หน่วยของกระแสไฟฟ้า (I)", ["Micro (μ)", "Milli (m)", "หน่วยพื้นฐาน (Base)", "Kilo (k)"], index=2)
            
        if st.button("🚀 คำนวณหาความต้านทาน (R)", use_container_width=True):
            st.snow()
            v_base = v_val * unit_multipliers[v_unit]
            i_base = i_val * unit_multipliers[i_unit]
            r_base = v_base / i_base
            
            st.markdown("### 📊 ผลลัพธ์การคำนวณ")
            col_res1, col_res2, col_res3 = st.columns(3)
            with col_res1:
                st.markdown(f'<div class="metric-card"><div class="metric-title">ความต้านทาน (Ω)</div><div class="metric-value">{r_base:,.2f}</div><div class="metric-unit">โอห์ม (Ω)</div></div>', unsafe_allow_html=True)
            with col_res2:
                st.markdown(f'<div class="metric-card" style="border-color:#10b981;"><div class="metric-title">ความต้านทาน (kΩ)</div><div class="metric-value" style="color:#10b981;">{r_base/1e3:,.4f}</div><div class="metric-unit">กิโลโอห์ม (kΩ)</div></div>', unsafe_allow_html=True)
            with col_res3:
                st.markdown(f'<div class="metric-card" style="border-color:#f59e0b;"><div class="metric-title">ความต้านทาน (MΩ)</div><div class="metric-value" style="color:#f59e0b;">{r_base/1e6:,.6f}</div><div class="metric-unit">เมกะโอห์ม (MΩ)</div></div>', unsafe_allow_html=True)

            st.latex(rf"R = \frac{{V}}{{I}} = \frac{{{v_val} \text{{ {v_unit.split()[
