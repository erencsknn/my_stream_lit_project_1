import streamlit as st
import requests
class App:
    def __init__(self):
        self.il = 'Bursa'
        self.ilce = 'Osmangazi'
        self.setup_ui()
        
        
    def setup_ui(self):
        st.title('Nöbetçi Eczane Bulma Uygulaması')
        
        
        self.il = st.text_input('İl', self.il)
        
        self.ilce = st.text_input('İlçe', self.ilce)
        
        self.run_button = st.button('Nöbetçi eczaneleri bul',on_click=self.eczane_listele)
    
    def get_duty_pharmacies(self):
        url = f'https://api.collectapi.com/health/dutyPharmacy?ilce={self.ilce}&il={self.il}'
        headers = {
            'content-type': "application/json",
            'authorization': "apikey 2gQPRhxWEdH48Kod6FpNaY:5JwGALsIsKIWwhZyto34kP"
    }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()['result']
        else:
            return st.write('Bir hata oluştu.')
        
    def eczane_listele(self):
        duty_pharmacies = self.get_duty_pharmacies()
        if duty_pharmacies:
            for pharmacy in duty_pharmacies:
                st.write(f"{pharmacy['name']} - {pharmacy['address']} - {pharmacy['phone']}")
        else:
            st.error('Nöbetçi eczane bulunamadı veya bir hata oluştu.')

             
    

     

    
        
