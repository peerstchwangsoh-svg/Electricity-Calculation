import streamlit as str
import time

# ⚡ เอฟเฟกต์สายฟ้าโปรยทั่วจอ
str.snow()

# ใส่โค้ดแต่งสายฟ้าสีเหลือง
str.markdown(
    """
    <style>
    .snowflake { color: #ffeb3b !important; font-size: 24px !important; }
    .snowflake::after { content: "⚡" !important; }
    </style>
    """,
    unsafe_allow_html=True
)

# ตั้งค่าหน้าเว็บ (เขียนแบบบรรทัดเดียวจบเพื่อไม่ให้งงวงเล็บครับ)
str.set_page_config(page_title="Electrical Measurement App", page_icon="⚡", layout="wide")
# ส่วนหัวของเว็บไซต์
str.title("⚡ เว็บไซต์แอปพลิเคชันการวัดไฟฟ้า (Electrical Measurement)")
str.subheader("จัดทำส่งอาจารย์ | พัฒนาด้วย Python & Streamlit")
str.write("---")

# แถบเมนูด้านข้าง (Sidebar) สำหรับตัวเลือกที่หลากหลาย
menu = str.sidebar.selectbox(
    "เลือกฟังก์ชันการทำงาน (เมนูหลัก)",
    ["🏠 หน้าแรก & ทฤษฎีการวัด", "🧮 เครื่องคำนวณกฎของโอห์ม", "🔄 เครื่องแปลงหน่วยไฟฟ้า", "📟 จำลองหน้าปัดมัลติมิเตอร์", "📝 แบบทดสอบความรู้"]
)

# ----------------- หน้า 1: หน้าแรก & ทฤษฎี -----------------
if menu == "🏠 หน้าแรก & ทฤษฎีการวัด":
    str.header("📖 ความรู้เบื้องต้นเกี่ยวกับการวัดไฟฟ้า")
    str.write("การวัดไฟฟ้าเป็นสิ่งสำคัญในการวิเคราะห์และซ่อมบำรุงวงจร โดยมีปริมาณพื้นฐาน 3 อย่างคือ:")
    
    col1, col2, col3 = str.columns(3)
    with col1:
        str.info("**แรงดันไฟฟ้า (Voltage - V)**\n\nความต่างศักย์ที่ทำให้กระแสไหล หน่วยเป็น โวลต์ (V)")
    with col2:
        str.success("**กระแสไฟฟ้า (Current - I)**\n\nการไหลของประจุไฟฟ้าในวงจร หน่วยเป็น แอมแปร์ (A)")
    with col3:
        str.warning("**ความต้านทาน (Resistance - R)**\n\nตัวต้านทานการไหลของกระแส หน่วยเป็น โอห์ม (Ω)")

# ----------------- หน้า 2: เครื่องคำนวณ -----------------
elif menu == "🧮 เครื่องคำนวณกฎของโอห์ม":
    str.header("🧮 เครื่องคำนวณกฎของโอห์ม ($V = IR$)")
    
    calc_option = str.selectbox("คุณต้องการคำนวณหาค่าอะไร?", ["หา แรงดันไฟฟ้า (V)", "หา กระแสไฟฟ้า (I)", "หา ความต้านทาน (R)"])
    
    if calc_option == "หา แรงดันไฟฟ้า (V)":
        i = str.number_input("ป้อนค่า กระแสไฟฟ้า (I) [A]", min_value=0.0, value=1.0)
        r = str.number_input("ป้อนค่า ความต้านทาน (R) [Ω]", min_value=0.0, value=10.0)
        if str.button("คำนวณค่า V"):
            v = i * r
            str.success(f"⚡ แรงดันไฟฟ้า (V) = {v:.2f} โวลต์ (V)")
            
    elif calc_option == "หา กระแสไฟฟ้า (I)":
        v = str.number_input("ป้อนค่า แรงดันไฟฟ้า (V) [V]", min_value=0.0, value=220.0)
        r = str.number_input("ป้อนค่า ความต้านทาน (R) [Ω]", min_value=0.1, value=100.0)
        if str.button("คำนวณค่า I"):
            i = v / r
            str.success(f"🔌 กระแสไฟฟ้า (I) = {i:.4f} แอมแปร์ (A)")
            
    elif calc_option == "หา ความต้านทาน (R)":
        v = str.number_input("ป้อนค่า แรงดันไฟฟ้า (V) [V]", min_value=0.0, value=12.0)
        i = str.number_input("ป้อนค่า กระแสไฟฟ้า (I) [A]", min_value=0.001, value=0.5)
        if str.button("คำนวณค่า R"):
            r = v / i
            str.warning(f"📐 ความต้านทาน (R) = {r:.2f} โอห์ม (Ω)")

# ----------------- หน้า 3: แปลงหน่วย -----------------
elif menu == "🔄 เครื่องแปลงหน่วยไฟฟ้า":
    str.header("🔄 เครื่องแปลงหน่วยวัดไฟฟ้า (Unit Converter)")
    
    unit_type = str.radio("เลือกปริมาณไฟฟ้าที่ต้องการแปลง:", ["กระแสไฟฟ้า (A)", "แรงดันไฟฟ้า (V)", "ความต้านทาน (Ω)"])
    value = str.number_input("ใสตัวเลขที่ต้องการแปลงหน่วย:", value=1.0)
    
    from_unit = str.selectbox("จากหน่วย:", ["Micro (μ)", "Milli (m)", "หน่วยหลัก (Base)", "Kilo (k)", "Mega (M)"])
    to_unit = str.selectbox("แปลงเป็นหน่วย:", ["Micro (μ)", "Milli (m)", "หน่วยหลัก (Base)", "Kilo (k)", "Mega (M)"])
    
    # ตัวคูณแปลงหน่วยกลับเข้าสู่ Base Unit
    multipliers = {"Micro (μ)": 1e-6, "Milli (m)": 1e-3, "หน่วยหลัก (Base)": 1.0, "Kilo (k)": 1e3, "Mega (M)": 1e6}
    
    if str.button("แปลงหน่วย"):
        # แปลงเป็นหน่วยฐานก่อน แล้วค่อยแปลงไปหน่วยที่ต้องการ
        base_value = value * multipliers[from_unit]
        result = base_value / multipliers[to_unit]
        str.info(f"ผลลัพธ์: {value} {from_unit} = {result:,.6f} {to_unit}")

# ----------------- หน้า 4: มัลติมิเตอร์จำลอง -----------------
elif menu == "📟 จำลองหน้าปัดมัลติมิเตอร์":
    str.header("📟 เครื่องวัดมัลติมิเตอร์จำลอง (Multimeter Simulator)")
    str.write("เลือกการตั้งค่าปุ่มและสายวัดเพื่ออ่านค่า")
    
    mode = str.selectbox("1. เลือกโหมดหน้าปัด (Dial Mode):", ["DC Volts (V-)", "AC Volts (V~)", "Resistance (Ω)", "Current (mA)"])
    range_select = str.selectbox("2. เลือกย่านวัด (Range):", ["Auto", "200m", "2", "20", "200", "1000"])
    wire_black = str.checkbox("เสียบสายดำที่ช่อง COM (Common) 🟩", value=True)
    wire_red = str.selectbox("3. เสียบสายแดงที่ช่องไหน? 🟥", ["ยังไม่ได้เสียบ", "ช่อง V/Ω (วัดแรงดัน/ความต้านทาน)", "ช่อง 10A (วัดกระแสสูง)", "ช่อง mA (วัดกระแสต่ำ)"])
    
    if str.button("กดเพื่ออ่านค่าจากเครื่องวัด"):
        if not wire_black:
            str.error("❌ วัดค่าไม่ได้: คุณไม่ได้เสียบสายดิน/สายดำ (COM)!")
        elif wire_red == "ยังไม่ได้เสียบ":
            str.error("❌ วัดค่าไม่ได้: กรุณาเสียบสายวัดสีแดงด้วยครับ")
        elif mode in ["DC Volts (V-)", "AC Volts (V~)", "Resistance (Ω)"] and wire_red != "ช่อง V/Ω (วัดแรงดัน/ความต้านทาน)":
            str.error("❌ แจ้งเตือน: เสียบสายแดงผิดช่อง! โหมดนี้ต้องใช้ช่อง V/Ω")
        elif mode == "Current (mA)" and wire_red == "ช่อง V/Ω (วัดแรงดัน/ความต้านทาน)":
            str.error("💥 ฟิวส์ขาด!: เอาสายวัดแรงดันไปวัดกระแสในวงจรไม่ได้!")
        else:
            str.success(f"📊 ผลการจำลอง: หน้าจอแสดงผลทำงานปกติในโหมด {mode} ย่านวัด {range_select} (ระบบทำงานถูกต้องสำหรับการทดลอง)")

# ----------------- หน้า 5: แบบทดสอบ -----------------
elif menu == "📝 แบบทดสอบความรู้":
    str.header("📝 แบบทดสอบความรู้เรื่องการวัดไฟฟ้า")
    str.write("ลองตอบคำถามเพื่อทดสอบความเข้าใจ")
    
    q1 = str.radio("1. เครื่องมือชนิดใดใช้สำหรับวัด 'กระแสไฟฟ้า' โดยตรง?", ["โวลต์มิเตอร์", "แอมมิเตอร์", "โอห์มมิเตอร์"])
    q2 = str.radio("2. ถ้าต้องการวัดแรงดันไฟฟ้าตกคร่อม ต้องต่อเครื่องวัดแบบใดกับวงจร?", ["ต่ออนุกรม", "ต่อขนาน", "ต่อแบบผสม"])
    
    score = 0
    if str.button("ตรวจคำตอบ"):
        if q1 == "แอมมิเตอร์": score += 1
        if q2 == "ต่อขนาน": score += 1
        
        str.write(f"### คุณได้คะแนน {score} / 2 คะแนน")
        if score == 2:
            str.balloons()
            str.success("ยอดเยี่ยมมาก! คุณเข้าใจเรื่องการวัดไฟฟ้าเป็นอย่างดี")
        else:
            str.warning("ลองทบทวนบทเรียนในหน้าแรกดูอีกทีนะครับ!")# สมมติว่าเป็นปุ่มคำนวณเดิมของคุณ
if str.button("คำนวณค่าไฟฟ้า"):
    
    # ⚡ ใส่ตรงนี้เพื่อให้สายฟ้าโปรยลงมาตอนกดปุ่มสำเร็จ
    st.snow() 
    
    # โค้ดคำนวณของคุณ...
    st.success("คำนวณผลลัพธ์สำเร็จเรียบร้อยแล้ว!")