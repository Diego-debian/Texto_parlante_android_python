#*-* coding:utf-8 *-*
import kivy
from jnius import autoclass
import time
from plyer.platforms.android import activity
from kivy.uix.button import Button 
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.widget import Widget

class __TextoHablado__(App):
    def Configuracion(self):       
        #tts.setLanguage(local.ROOT)
        for i in range (1,5,1):
            self.tts.setLanguage(self.local.ROOT)
            try:
                
                self.tts.speak("yo soy el dispositivo de Diego debian", self.texto_hablado.QUEUE_ADD,None)
                print "se encontro pero no funciona"
                if True:
                    time.sleep(4)
                    
            except:
                #   time.sleep(1)
                print "no se encontro local"
                pass
                
    def ac_btn1(self, *args):
        self.Configuracion()
        pass
        
    def Boton1(self):
        btn1 = Button()
        btn1.text = "Hablar"
        btn1.pos = 100, 100 
        btn1.size_hint= 0.7, 0.4
        btn1.height = '48dp'
	btn1.bind(on_press=self.ac_btn1)
        self.Mi_Widget.add_widget(btn1)


    def build(self):
        self.Mi_Widget= Widget()
        self.local =autoclass('java.util.Locale')
        actividadPython = autoclass('org.renpy.android.PythonActivity')
        self.texto_hablado = autoclass('android.speech.tts.TextToSpeech')
        self.tts = self.texto_hablado(actividadPython.mActivity,None)
        self.Boton1()
        return self.Mi_Widget

if __name__=='__main__':
    __TextoHablado__().run()

