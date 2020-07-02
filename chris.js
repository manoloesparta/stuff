const fs = require('fs');
const rs = require("reddit-simple")
const fb = require("facebook-chat-api")
const im = require('image-downloader')

const email = process.env.email
const pass = process.env.pass
const thread = process.env.thread

if(email == undefined || pass == undefined) { 
  return console.log("Export email, pass, and thread env vars")
}

rs.RedditSimple.TopPost("programmerHumor").then(res => {
  const data = res[0].data
  const img = data.url
  const title = data.title

  const options = {
    url: img,
    dest: __dirname + "/image.jpg"
  }

  im.image(options).then(({ filename }) => {
    console.log('Saved to', filename)
  })
  .catch((err) =>{
    return console.error(err) 
  })

  fb({email: email, password: pass}, (err, api) => {
    if(err) {
      return console.error(err)
    }

    msg = {
      body: title,
      attachment: fs.createReadStream(__dirname + "/image.jpg")
    }
	 
	  api.sendMessage(msg, thread)
  })
})