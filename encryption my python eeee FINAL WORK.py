from appJar import gui




registered_users = {}


def press(button):
    if button == "Cancel":
        app.stop()
    elif button == "Submit":
      
        register_user(app.getEntry("Create Username"), app.getEntry("Create Password"))
    elif button == "Already Have an Account, Login":
        open_login_window()

def register_user(username, password):
    if username and password:
        registered_users[username] = password
        print("User", username, "registered successfully!")
        open_welcome_window()
    else:
        print("Please provide both username and password.")

def open_login_window():
    app.showSubWindow("Login Window")

def login(button):
    username = app.getEntry("Login Username")
    password = app.getEntry("Login Password")
    if username in registered_users and registered_users[username] == password:
        print("Logged In Successfully")
        open_welcome_window()
    else:
        print("Log In Unsuccessful")

def open_welcome_window():
    app.showSubWindow("Encrypt or Decrypt?")


app = gui("Sign Up Window", "1077x988")
app.setBg("LavenderBlush")
app.setFont(size=34, family="Times", underline=False, slant="italic")
app.setButtonFont(size=14, family="Verdana", underline=False, slant="roman")


app.addFlashLabel("title", "Welcome to frog encryptions")
app.startLabelFrame("frog")
app.addImage("frog", "frog-frog-love.gif")
app.stopLabelFrame()
app.setFlashLabelBg("title", "cornsilk")
app.setFlashLabelFg("title", "cornsilk")
app.addLabel(".")
app.setLabelBg(".", "CornflowerBlue")
app.setLabelFg(".", "CornflowerBlue")
app.addLabel("..")
app.setLabelBg("..", "Lavender")
app.setLabelFg("..", "Lavender")
app.addLabel("...")
app.setLabelBg("...", "Pink")
app.setLabelFg("...", "Pink")
app.addLabel("....")
app.setLabelBg("....", "LightSteelBlue")
app.setLabelFg("....", "LightSteelBlue")
app.addLabelEntry("Create Username")
app.addLabelSecretEntry("Create Password")
app.setFocus("Create Username")


app.addButtons(["Submit", "Already Have an Account, Login", "Cancel"], press)


app.startSubWindow("Login Window")
app.setBg("Ivory")
app.setSize("650x450")
app.addFlashLabel("t", "Welcome to the Login Window")
app.addLabel("aaaaaaaaaaaaaaaaaaaaaaaaaaaa")
app.setLabelBg("aaaaaaaaaaaaaaaaaaaaaaaaaaaa", "LavenderBlush")
app.setLabelFg("aaaaaaaaaaaaaaaaaaaaaaaaaaaa", "LavenderBlush")
app.addLabel("abbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
app.setLabelBg("abbbbbbbbbbbbbbbbbbbbbbbbbbbbb", "AntiqueWhite")
app.setLabelFg("abbbbbbbbbbbbbbbbbbbbbbbbbbbbb", "AntiqueWhite")
app.addLabel("abccccccccccccccccccccccccccccccccc")
app.setLabelBg("abccccccccccccccccccccccccccccccccc", "Linen")
app.setLabelFg("abccccccccccccccccccccccccccccccccc", "Linen")
app.addLabel("abcddddddddddddddddddddddddddddd")
app.setLabelBg("abcddddddddddddddddddddddddddddd", "MistyRose")
app.setLabelFg("abcddddddddddddddddddddddddddddd", "MistyRose")
app.addLabel("login_title", "Login")
app.addLabelEntry("Login Username")
app.addLabelSecretEntry("Login Password")
app.addButton("Login Submit", login)
app.stopSubWindow()


app.startSubWindow("Encrypt or Decrypt?", modal=True)
app.setBg("LavenderBlush")
app.setSize("800x700")
app.addFlashLabel("welcome_title", "Welcome to Frog ENCRPYTIONS!")
app.addFlashLabel("welcome_titlee", "Have a nice stay!")
app.addLabel("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
app.setLabelBg("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv", "Linen")
app.setLabelFg("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv", "Linen")
app.addLabel("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
app.setLabelBg("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv", "MistyRose")
app.setLabelFg("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv", "MistyRose")
def show_decrypter(btn):
    app.showSubWindow("Decrypter")


def show_encrypter(btn):
    app.showSubWindow("Encrypter")
app.addButtons(["Decrypter", "Encrypter", "Close App"], [show_decrypter, show_encrypter, app.stop])

app.startSubWindow("Decrypter", modal=True)
app.setBg("LavenderBlush")
app.setSize("700x500")
app.addFlashLabel("DecryptTitle", "Welcome to the decrypter!")
app.addLabel("fffffffffffffffffffffffffffffff")
app.setLabelBg("fffffffffffffffffffffffffffffff", "CornflowerBlue")
app.setLabelFg("fffffffffffffffffffffffffffffff", "CornflowerBlue")
app.addLabel("ffffffffffffffffffffffffffffffffff")
app.setLabelBg("ffffffffffffffffffffffffffffffffff", "Lavender")
app.setLabelFg("ffffffffffffffffffffffffffffffffff", "Lavender")
app.addButton("Closee", app.stop)

def decode():
    message = app.getEntry("inputText=")
    decoded = ""
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,.?"
    code = "qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM ,.?"


    length = len(message)
    for i in range(0,length): 
        letter = message[i]
        counter = 0
        while letter !=code[counter]:
         counter = counter+1
        newletter = alphabet[counter]
        decoded = decoded + newletter
    app.setLabel("output=", "Decrypted Text is..." + decoded)
app.addLabelEntry("inputText=")
app.addButton("Decryption", decode)
app.addLabel("output=")

app.stopSubWindow()


app.startSubWindow("Encrypter", modal=True)
app.setBg("LavenderBlush")
app.setSize("700x500")
app.addFlashLabel("EncryptTitle", "Welcome to the encrypter!")
app.addLabel("rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
app.setLabelBg("rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr", "CornflowerBlue")
app.setLabelFg("rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr", "CornflowerBlue")
app.addLabel("rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
app.setLabelBg("rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr", "Lavender")
app.setLabelFg("rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr", "Lavender")
app.addButton("Closeeee", app.stop)
def encode():
    message = app.getEntry("inputText")
    encoded = ""

    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ,.?"
    code = "qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM ,.?"
    


    length = len(message)
    for i in range(0,length): 
        letter = message[i]
        counter = 0
        while letter !=alphabet[counter]:
         counter = counter+1
        newletter = code[counter]
        encoded = encoded + newletter

    app.setLabel("output", "Encrypted Text is..." + encoded)
app.addLabelEntry("inputText")
app.addLabel("output")

app.addButton("Encryption", encode)
app.stopSubWindow()

app.go()
