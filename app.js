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
	res.send("This is the home page");
});




// var travelData = [["17:02:06", 37], ["17:03:07", 36], ["17:04:06", 37], ["17:05:07", 36], ["17:06:06", 36], ["17:07:07", 37], ["17:08:07", 37], 
// 			["17:09:06", 38], ["17:10:06", 37], ["17:11:07", 38], ["17:12:06", 37], ["17:13:07", 37], ["17:14:06", 37], ["17:15:06", 37], ["17:16:07", 37], 
// 			["17:17:07", 38], ["17:18:06", 38], ["17:19:07", 39], ["17:20:07", 39], ["17:21:06", 39], ["17:22:06", 39], ["17:23:06", 38], ["17:24:06", 38], 
// 			["17:25:07", 37], ["17:26:07", 38], ["17:27:06", 38], ["17:28:07", 37], ["17:29:06", 37], ["17:30:07", 37], ["17:31:06", 37], ["17:32:07", 37], 
// 			["17:33:06", 35], ["17:34:06", 34], ["17:35:06", 34], ["17:36:06", 34], ["17:37:06", 34], ["17:38:06", 33], ["17:39:06", 33], ["17:40:06", 33], 
// 			["17:41:06", 32]];

// //Generating X and Y axis arrays to plug into the graphing code
// var xAxis = [];
// var yAxis = [];

// for(var i = 0; i < travelData.length; i++){
// 	xAxis[i] = travelData[i][0];
// 	yAxis[i] = travelData[i][1];
// }

// //Generating a table to display the data
// var table = "<tr><td><strong>Time of Day</strong></td><td><strong>Travel Time</strong></td></tr>";
// for(var r = 0; r < travelData.length; r++){
// 	table += '<tr>';
// 	for(var c = 0; c < 2; c++){
// 		table += '<td>' + travelData[r][c] + '</td>';
// 	}
// 	table += '</tr>';
// }
// //writes a string to the HTML wherever the script tag is included.
// document.write("<div class='container'><table class='table table-striped table-bordered'>" + table + "</table></div>");




//starts server on port 3000
app.listen(3000, function(){
	console.log("Server: spinning up on route 3000");
});