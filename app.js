require("dotenv").config();

var express = require("express"),
	app     = express(),
	mongoose = require("mongoose"),
	bodyParser = require("body-parser");

mongoose.connect("mongodb://localhost/traffic_app", {useNewUrlParser: true, useUnifiedTopology: true, useFindAndModify: false});

app.use(bodyParser.urlencoded({extended:true}));
app.set("view engine", "ejs");
//app.use(express.static(_dirname + "/public"));

//defining a schema for the data model
var dataSchema = new mongoose.Schema({
	route: String,
	timeOfDay: Number,
	travelTime: Number
});

//creating schema under Data variable
var Data = mongoose.model("Data", dataSchema);


//renders a 'homepage' under the default '/' route
app.get("/", function(req, res){
	res.render("home");
});

//starts server on port 3000
app.listen(3000, function(){
	console.log("Server: spinning up on route 3000");
});