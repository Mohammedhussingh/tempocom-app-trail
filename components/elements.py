def arrow_element():
    return f"""<div style='display: flex; justify-content: center; margin: 30px 0;'>
    <div style='display: flex; flex-direction: column; align-items: center;'>
        <div style='width: 4px; height: 100px; background: linear-gradient(to bottom, #0077b6, #6a0dad); border-radius: 2px;'></div>
        <div style='width: 0; height: 0; border-left: 10px solid transparent; border-right: 10px solid transparent; border-top: 15px solid #6a0dad;'></div>
    </div>
</div>"""

def end_page():
    return f"""<div style='text-align: center; color: #666; margin-top: 50px;'>© 
        2025 TEMPOCOM - All rights reserved
    </div>"""