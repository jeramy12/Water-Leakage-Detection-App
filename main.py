import pandas as pd
import kivy
kivy.require('2.0.0')
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.garden.notification import Notification
import socket
import threading

screen_helper ="""
MainScreen:
	id: screen_manager
	lockscreen:lockscreen
	mainscreen:mainscreen
	LockScreen:
		id:lockscreen
		name: "lock"
		manager: screen_manager
	Main: 
		id: mainscreen
		name: "main"
		manager: screen_manager
		


	
	
<LockScreen>:
	Screen:
		display: entry
		rows: 5
		padding: 10
		spacing: 10
		FitImage:
			source: "Background.jpg"
		FitImage:
			source: "PicsArt_09-08-02.07.04.png"
			size_hint_x : None
			size_hint_y : None
			pos_hint : {"center_x":.5, "center_y":.8}
		MDTextFieldRect:
			id: entry
			hint_text : "Enter Your PIN"
			size_hint_x : .9
			size_hint_y:.06
			width : 200
			halign: "center"
			font_size : 20
			pos_hint : {"center_x":.5, "center_y":.65}
			color_active : [1,1,1,1]
			password : True
			input_filter: "int"
			normal_color : [255/255,255/255,255/255.1]
			multiline: False
			readonly: True
			
		MDLabel:
			text: ""
			id: lock_label
			theme_text_color: "Error"
			halign: "center"
			pos_hint : {"center_x":.5, "center_y":.6}
			multiline: False
		MDRoundFlatButton:
			text: "1"
			theme_text_color: "Custom"
			text_color: [255/255,255/255,255/255,1]
			md_bg_color:  [93/255,211/255,217/255,1]
			pos_hint : {"center_x":.2, "center_y":.5}
			line_width: 1
			font_size: 15
			line_color: [255,255,255,1]
			on_press:
				entry.text += self.text
		MDRoundFlatButton:
			text: "2"
			theme_text_color: "Custom"
			text_color: [255/255,255/255,255/255,1]
			md_bg_color:  [93/255,211/255,217/255,1]
			pos_hint : {"center_x":.5, "center_y":.5}
			line_width: 1
			font_size: 15
			line_color: [255,255,255,1]
			on_press:
				entry.text += self.text
		MDRoundFlatButton:
			text: "3"
			theme_text_color: "Custom"
			text_color: [255/255,255/255,255/255,1]
			md_bg_color:  [93/255,211/255,217/255,1]
			pos_hint : {"center_x":.8, "center_y":.5}
			line_width: 1
			font_size: 15
			line_color: [255,255,255,1]
			on_press:
				entry.text += self.text
		MDRoundFlatButton:
			text: "4"
			theme_text_color: "Custom"
			text_color: [255/255,255/255,255/255,1]
			md_bg_color:  [93/255,211/255,217/255,1]
			pos_hint : {"center_x":.2, "center_y":.4}
			line_width: 1
			font_size: 15
			line_color: [255,255,255,1]
			on_press:
				entry.text += self.text
		MDRoundFlatButton:
			text: "5"
			theme_text_color: "Custom"
			text_color: [255/255,255/255,255/255,1]
			md_bg_color:  [93/255,211/255,217/255,1]
			pos_hint : {"center_x":.5, "center_y":.4}
			line_width: 1
			font_size: 15
			line_color: [255,255,255,1]
			on_press:
				entry.text += self.text
		MDRoundFlatButton:
			text: "6"
			theme_text_color: "Custom"
			text_color: [255/255,255/255,255/255,1]
			md_bg_color:  [93/255,211/255,217/255,1]
			pos_hint : {"center_x":.8, "center_y":.4}
			line_width: 1
			font_size: 15
			line_color: [255,255,255,1]
			on_press:
				entry.text += self.text
		MDRoundFlatButton:
			text: "7"
			theme_text_color: "Custom"
			text_color: [255/255,255/255,255/255,1]
			md_bg_color:  [93/255,211/255,217/255,1]
			pos_hint : {"center_x":.2, "center_y":.3}
			line_width: 1
			font_size: 15
			line_color: [255,255,255,1]
			on_press:
				entry.text += self.text
		MDRoundFlatButton:
			text: "8"
			theme_text_color: "Custom"
			text_color: [255/255,255/255,255/255,1]
			md_bg_color:  [93/255,211/255,217/255,1]
			pos_hint : {"center_x":.5, "center_y":.3}
			line_width: 1
			font_size: 15
			line_color: [255,255,255,1]
			on_press:
				entry.text += self.text
		MDRoundFlatButton:
			text: "9"
			theme_text_color: "Custom"
			text_color: [255/255,255/255,255/255,1]
			md_bg_color:  [93/255,211/255,217/255,1]
			pos_hint : {"center_x":.8, "center_y":.3}
			line_width: 1
			font_size: 15
			line_color: [255,255,255,1]
			on_press:
				entry.text += self.text
		MDRoundFlatButton:
			text: "0"
			theme_text_color: "Custom"
			text_color: [255/255,255/255,255/255,1]
			md_bg_color:  [93/255,211/255,217/255,1]
			pos_hint : {"center_x":.5, "center_y":.2}
			line_width: 1
			font_size: 15
			line_color: [255,255,255,1]
			on_press:
				entry.text += self.text
		MDRoundFlatButton:
			text:"Clear"
			theme_text_color: "Custom"
			text_color: [255/255,255/255,255/255,1]
			md_bg_color:  [93/255,211/255,217/255,1]
			pos_hint : {"center_x":.8, "center_y":.2}
			line_width: 1
			font_size: 15
			line_color: [255,255,255,1]
			on_press:
				entry.text = ""
		MDRoundFlatButton:
			text:"OK"
			theme_text_color: "Custom"
			text_color: [255/255,255/255,255/255,1]
			md_bg_color:  [93/255,211/255,217/255,1]
			pos_hint : {"center_x":.2, "center_y":.2}
			line_width: 1
			font_size: 15
			line_color: [255,255,255,1]
			on_release:
				root.Login(entry.text)
			

<Main>
	Screen:
		FitImage:
			source: "Background.jpg"
		MDToolbar:
			id: toolbar
			pos_hint: {"top":1}
			md_bg_color:  [0/255,242/255,254/255,0]
			left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
		
		MDNavigationLayout:
			x:toolbar.height
			ScreenManager:
				id: screen_manager
				Screen:
					name:"scr 1"
					MDLabel:
						text:"Notification"
						font_size:20
						size_hint_x: 1
						size_hint_y: None
						halign: "center"
						pos_hint : {"center_x":.5, "center_y":.95}
						
					FitImage:
						source: "PicsArt_09-08-02.07.04.png"
						size_hint_x : None
						size_hint_y : None
						pos_hint : {"center_x":.5, "center_y":.8}
					MDLabel:
						id:lbl_leak
						text:""
						font_size:15
						size_hint_x: .9
						size_hint_y: .4
						halign: "center"
						pos_hint : {"center_x":.5, "center_y":.5}
						md_bg_color:  [93/255,211/255,217/255,1]
						
					MDIconButton:
						icon:"power"
						pos_hint : {"center_x":.5, "center_y":.15}
						md_bg_color: [19/255,84/255,122/255,1]
						user_font_size: "60sp"
						line_width: 2
						on_press:
							root.power_button()
					
				Screen:
					name:"scr 2"
					id: scr2
					MDLabel:
						text:"Set PIN Password"
						font_size:20
						size_hint_x: 1
						size_hint_y: None
						halign: "center"
						pos_hint : {"center_x":.5, "center_y":.95}
					FitImage:
						source: "PicsArt_09-08-02.07.04.png"
						size_hint_x : None
						size_hint_y : None
						pos_hint : {"center_x":.5, "center_y":.8}
					MDTextFieldRect:
						id : C_pass
						hint_text : "Enter PIN"
						size_hint_x: None
						size_hint_y:.06
						width : 200
						font_size : 20
						pos_hint : {"center_x":.5, "center_y":.6}
						color_active : [1,1,1,1]
						password : True
						normal_color : [255/255,255/255,255/255.1]
						input_filter: "int"
					MDTextFieldRect:
						id: C_confirmpass
						hint_text : "Confirm PIN"
						size_hint_x : None
						size_hint_y:.06
						width : 200
						font_size : 20
						pos_hint : {"center_x":.5, "center_y":.5}
						color_active : [1,1,1,1]
						password : True
						input_filter: "int"
						normal_color : [255/255,255/255,255/255.1]
					MDLabel:
						text: ""
						id: pin_label
						theme_text_color: "Error"
						halign: "center"
						pos_hint : {"center_x":.5, "center_y":.4}
						multiline: False
					MDRaisedButton:
						text: "Confirm"
						md_bg_color:  [93/255,211/255,217/255,1]
						pos_hint : {"center_x":.5, "center_y":.3}
						line_color: [0,0,0,1]
						on_press:
							root.create_pin()
						
						
				Screen:
					name:"scr 3"
					MDLabel:
						text:"HELP?"
						theme_text_color : "Error"
						font_size:20
						size_hint_x: 1
						size_hint_y: None
						halign: "center"
						pos_hint_x:None
						pos_hint: {"center_y":.9}
					MDLabel:
						text:"Main Screen"
						theme_text_color: "Custom"
						text_color : [19/255,84/255,122/255,1]
						font_size:20
						size_hint_x: 1
						size_hint_y: None
						halign: "left"
						pos_hint: {"center_y":.85}
					MDLabel:
						text:"Box- User can able to see the notification about the leaks, what cable, where is the location and the meter that the leaks occured."
						font_size:15
						size_hint_x: .9
						size_hint_y: .2
						halign: "center"
						halign: "left"
						pos_hint: {"center_x":.5,"center_y":.75}
					MDLabel:
						text:"Turn On/Off - User can press the On button so that they can open the water flow after the leak has been resolved. You can also press again the button if you want to close the water flow when you are going to somewhere."
						font_size:15
						size_hint_x: .9
						size_hint_y: .2
						halign: "center"
						halign: "left"
						pos_hint: {"center_x":.5,"center_y":.55}
					MDLabel:
						text:"Set PIN"
						theme_text_color: "Custom"
						text_color : [19/255,84/255,122/255,1]
						font_size:20
						size_hint_x: 1
						size_hint_y: None
						halign: "left"
						pos_hint: {"center_y":.40}
					MDLabel:
						text:"Create PIN - User can create their own PIN if necessary. It is used to avoid someone using it without permission or for playtime(especialy children)."
						font_size:15
						size_hint_x: .9
						size_hint_y: .2
						halign: "center"
						halign: "left"
						pos_hint: {"center_x":.5,"center_y":.30}
			MDNavigationDrawer:
				id:nav_drawer
				ContentNavigationDrawer:
					screen_manager:screen_manager
					nav_drawer:nav_drawer
					
				
				
<ContentNavigationDrawer>:
	orientation:"vertical"
	padding:"5dp"
	spacing:"5dp"
	FitImage:
		source: "PicsArt_09-08-02.07.04.png"
		size_hint_x : None
		size_hint_y : None
		pos_hint : {"center_x":.2}
		
	MDLabel:
		text: "SOLUSYUN KING TAGAS"
		font_size:25
		size_hint_y:None
		theme_text_color: "Custom"
		text_color : [19/255,84/255,122/255,1]
		height: self.texture_size[1]
	ScrollView:
		MDList:
			OneLineListItem:
				id: item1
				text: "Notification"
				theme_text_color: "Custom"
				text_color : [93/255,211/255,217/255,1]
				on_release:
					item3.text_color = [0/255,0/255,0/255,1]
					item2.text_color = [0/255,0/255,0/255,1]
					item1.text_color = [93/255,211/255,217/255,1] if item1.text_color == [93/255,211/255,217/255,1] else [93/255,211/255,217/255,1]
					root.nav_drawer.set_state("close")
					root.screen_manager.current = "scr 1"
				
			OneLineListItem:
				id: item2
				text_color : [0/255,0/255,0/255,1]
				text: "Set Pin Password"
				theme_text_color: "Custom"
				on_release:
					item3.text_color = [0/255,0/255,0/255,1]
					item1.text_color = [0/255,0/255,0/255,1]
					item2.text_color = [93/255,211/255,217/255,1] if item2.text_color == [93/255,211/255,217/255,1] else [93/255,211/255,217/255,1]
					root.nav_drawer.set_state("close")
					root.screen_manager.current = "scr 2"
					
			OneLineListItem:
				id: item3
				theme_text_color: "Custom"
				text_color: [0/255,0/255,0/255,1]
				text: "Help"
				on_release:
					item1.text_color = [0/255,0/255,0/255,1]
					item2.text_color = [0/255,0/255,0/255,1]
					item3.text_color = [93/255,211/255,217/255,1] if item3.text_color == [93/255,211/255,217/255,1] else [93/255,211/255,217/255,1]
					root.nav_drawer.set_state("close")
					root.screen_manager.current = "scr 3"

	
			


"""
df = pd.read_csv('pin.csv')

class LockScreen(Screen):
    def __init__(self,**kwargs):
        super(LockScreen, self).__init__(**kwargs)

    def loop(self):
       i=0
       a=None
       while i==0:
            data = self.manager.s.recv(32).decode('ascii')
            print(data)
            if data == 'a':
                main_screen = self.manager.get_screen('main')
                main_screen.ids.lbl_leak.text = f"LEAKS OCCUR!!\n\nLocation: leftside of the bathroom\n The valve has turned off"
                Notification().open(
                title="Leaks Occur!",
                icon="logo/PicsArt_09-08-02.07.04.png",
                message="\nLocation: left side of the bathroom",
                timeout=1000,
                )
                break
            elif data == 'b':
                main_screen = self.manager.get_screen('main')
                main_screen.ids.lbl_leak.text = f"LEAKS OCCUR!!\n\nLocation: center of the bathroom\n The valve has turned off"
                Notification().open(
                title="Leaks Occur!",
                icon="logo/PicsArt_09-08-02.07.04.png",
                message=f"\nLocation: rightside of the bathroom",
                timeout=1000,
                )
                break
            elif data == 'c':
                main_screen = self.manager.get_screen('main')
                main_screen.ids.lbl_leak.text = f"LEAKS OCCUR!!\n\nLocation: rightside of the bathroom\n The valve has turned off"
                Notification().open(
                title="Leaks Occur!",
                icon="logo/PicsArt_09-08-02.07.04.png",
                message="\nLocation: right side of the bathroom",
                timeout=1000,
                )
                break
            else:
                continue
    def Login(self, pin):
        Pin = int(df.Password[0])
        pin = pin
        if float(pin) == Pin:
              # Create a socket object
            try:
                host = '192.168.43.173'
                port = 8888  # Reserve a port for your service
                self.manager.s.connect((host, port))
                self.manager.current = "main"
                # self.a = threading.Thread(target=self.a)
                self.thread = threading.Thread(target=self.loop)
                # self.a.start()
                self.thread.start()
            except:
                self.ids.lock_label.text = f"Hardware is not available"
        else:
            self.ids.lock_label.text = f" Incorrect Password"






class Main(Screen):
    pass

    def power_button(self):

        outp = "1"
        self.manager.s.sendall(outp.encode())
        self.ids.lbl_leak.text = f""
    def create_pin(self):
        pwd = self.ids.C_pass.text
        pwdcon = self.ids.C_confirmpass.text
        if pwd != "" and pwdcon != "":
            if pwd == pwdcon:
                user = pd.DataFrame([pwd], columns=["Password"])
                print(user)
                user.to_csv('pin.csv', mode='a', header=False, index=False)
                self.ids.pin_label.text = f"Password successfuly saved"
                self.ids.C_pass.text = ""
                self.ids.C_confirmpass.text = ""
            else:
                self.ids.pin_label.text = f"Password didn't match"
        else:
            self.ids.pin_label.text = f'Please complete all fields'

class ContentNavigationDrawer(BoxLayout):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class MainScreen(ScreenManager):
    s = socket.socket()
    lockscreen = ObjectProperty()
    mainscreen = ObjectProperty()

class SolusyunKingTagas(MDApp):

    def build(self):
        ckv = Builder.load_string(screen_helper)
        if df.empty == True:
            return ckv
        else:
            return ckv




if __name__ == '__main__':
    SolusyunKingTagas().run()