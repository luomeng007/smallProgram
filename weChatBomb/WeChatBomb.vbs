set wshshell=wscript.createobject("wscript.shell") 
wshshell.AppActivate"要发送的人的昵称" 
wscript.sleep 2000
for i=1 to 101
wscript.sleep 300
wshshell.sendKeys "^v" 
wshshell.sendKeys i 
wshshell.sendKeys "%s" 
next