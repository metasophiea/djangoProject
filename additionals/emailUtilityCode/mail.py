import os

def sendMail(origin, destination, header, body):
    command = "echo "
    command += "\"" + body.replace('"','\\"') + "\""
    command += " | "
    command += "mail "
    command += "-s \"" + header.replace('"','\\"') + "\" "
    command += "-aFrom:" + origin.replace('"','\\"') + " "
    command += destination.replace('"','\\"')

    os.system(command)