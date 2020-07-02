const fs = require('fs');
const rs = require("reddit-simple")
const fb = require("facebook-chat-api")
const im = require('image-downloader')

const email = process.env.email
const pass = process.env.pass
const thread = process.env.thread
const imgpath = __dirname + "/image.jpg"

if(email == undefined || pass == undefined) { 
  return console.log("Export email, pass, and thread env vars")
}

rs.RedditSimple.TopPost("programmerHumor").then(res => {
  const data = res[0].data
  const img = data.url
  const title = data.title

  const options = {
    url: img,
    dest: imgpath
  }

  im.image(options)

  fb({email: email, password: pass}, (err, api) => {
    msg = {
      body: title,
      attachment: fs.createReadStream(imgpath)
    }

    api.sendMessage(msg, thread)
  })
})