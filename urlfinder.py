from burp import IBurpExtender,ITab
from java.io import PrintWriter
from java.lang import RuntimeException
from javax.swing import JPanel, JButton, JLabel, JTextField,BoxLayout, JTextArea
from java.awt import BorderLayout, Color

class BurpExtender(IBurpExtender,ITab):
    

    def getTabCaption(self):
      return "Url Finder"

    def getUiComponent(self):
      panel = JPanel(BorderLayout())
      panel.setLocation(100,100)
      panel.setLayout(None)


      lbl1 = JLabel("Insert URL")
      lbl1.setBounds(60,20,100,40)
      txt1 = JTextField(100)
      txt1.setBounds(140,20,600,40)
      

      def btn1Click(event):
      

	import requests
	from bs4 import BeautifulSoup


	url=requests.get("http://"+str(txt1.text))
#	a=requests.get(str(txt1.text)) 
        req=url.text
	links=[]
	soup = BeautifulSoup(url.text, 'html.parser')
	for link in soup.find_all('a'):
        	links.append(link.get('href'))

	links=((str(links).replace("[","")).replace("]","")).replace("u'","'")

	txt2.text=links #set info por table2
	txt2.editable= False
	txt2.wrapStyleWord = True
	txt2.lineWrap = True
	text2.aligmentx = Component.LEFT_ALIGMENT
	txt2.size(300,1)


        return

        


      btn = JButton("Click", actionPerformed=btn1Click)
      btn.setBounds(400,80,60,30)
      panel.add(lbl1,BorderLayout.CENTER)
      panel.add(txt1,BorderLayout.CENTER)
      panel.add(btn,BorderLayout.CENTER)

      lbl2 = JLabel("Output URLs")
      lbl2.setBounds(60,80,150,40)

      txt2= JTextArea()
      txt2.setBounds(140,120,600,600)
      txt2.setBackground(Color.WHITE); # set table color, if you want

      panel.add(lbl2,BorderLayout.CENTER)
      panel.add(txt2,BorderLayout.CENTER)


      return panel




    
    def	registerExtenderCallbacks(self, callbacks):
        
        callbacks.setExtensionName("Url Finder")
        callbacks.printOutput("Loading...made by michelle")
        callbacks.addSuiteTab(self)


        return
