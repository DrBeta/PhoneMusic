from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)


@app.route("/voice", methods=['GET', 'POST'])
def voice():

    resp = VoiceResponse()

    resp.play('https://files.freemusicarchive.org/storage-freemusicarchive-org/music/ccCommunity/Chad_Crouch/Field_Report_Vol_II_Reed_Canyon_Instrumental/Chad_Crouch_-_05_-_Song_Sparrow_Serenade_Instrumental.mp3', loop=1)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)