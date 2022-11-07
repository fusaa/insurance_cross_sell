function onOpen(){
	var ui = SpreadsheetApp.getUi();
	ui.createMenu('Get Scores')
		.addItem('Get Prediction','PredictAll')
		.addToUi();
}

// heroku link:
url_production = 'https://cross-sell-insurance-api.herokuapp.com' //predict'
// Helper func
function ApiCall(data, endpoint){
	// var url = 'https://' + host_production + endpoint;
  var url = url_production + endpoint;
	var payload = JSON.stringify(data)
	var options = {'method':'POST', 'contentType':'application/json', 'payload':payload};
	Logger.log(url)
	Logger.log(options)
	var response = UrlFetchApp.fetch( url, options);
	// with response:
	var rc = response.getResponseCode();
	var responseText = response.getContentText();
	if ( rc!== 200 ){
		Logger.log('Response (%s) %s', rc, responseText);
	}
	else{
		prediction = JSON.parse(responseText);
    Logger.log(prediction)
	}
	return prediction
}

function PredictAll(){
	var ss = SpreadsheetApp.getActiveSheet();
	var titleColumns = ss.getRange('A1:J1').getValues()[0];
	var lastRow = ss.getLastRow()
	
	var data = ss.getRange('A2' + ':' + 'J'+ lastRow).getValues();

	// run across whole spreadsheet
	for ( row in  data) {
		var json = new Object();
		// now on columns:
		for ( var j = 0; j < titleColumns.length; j++){
			json[titleColumns[j]] = data[row][j];
      Logger.log(json[titleColumns[j]])
		};
    // json list
    var json_send = new Object();
    json_send['id'] = json['id']
    json_send['gender'] = json['gender']
    json_send['age'] = json['age']
    json_send['region_code'] = json['region_code']
    json_send['previously_insured'] = json['previously_insured']
    json_send['vehicle_age'] = json['vehicle_age']
    json_send['vehicle_damage'] = json['vehicle_damage']
    json_send['annual_premium'] = json['annual_premium']
    json_send['policy_sales_channel'] = json['policy_sales_channel']
    json_send['vintage'] = json['vintage']
 

	Logger.log( json_send);

  Logger.log(lastRow)
  Logger.log(titleColumns)

pred = ApiCall( json_send, '/predict');
ss.getRange(Number(row)+2, 11).setValue( pred[0]['prediction'] )
Logger.log(pred[0]['score'])
}
}
