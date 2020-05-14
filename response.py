#/usr/bin/python3

response = {
       "COMMAND1" : "RESPONSE1",
       "COMMAND2" : "RESPONSE2"
    }

def chat(command):
        try:
            ans = response[command]
            return ans
        
        except:
            return None
