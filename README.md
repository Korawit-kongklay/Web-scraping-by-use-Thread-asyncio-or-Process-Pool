# Web scraping by use asyncio

ติดตั้งโมดูลที่จำเป็น
pip install requests aiohttp asyncio

วิธีการทำงาน
web scraping ทำงานโดยการรดึง เนื้อหา จาก url ที่กำหนดไว้ จากนั้นวัดเป็นจำนวน byte แล้วบันทึกเวลาการทำงานทั้งหมด เพื่อเปรียบเทียบระหว่างการใช้ แบบ ayncio และไม่ใช้ ayncio 
