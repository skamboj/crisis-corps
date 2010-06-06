//FB.api('/me', function(response) {
//  var msg = "";
//  for(var i in response) {
//	  msg += "Key: "+i+" - Value: "+response[i]+"\n";
//  }
//  alert(msg);
//});

//var query = FB.Data.query('select name, uid from user where uid={0}', user_id);
//query.wait(function(rows) {
//	alert('Your name is ' + rows[0].name);
//});


// initialize the library with the API key
  FB.init({
	  apiKey: '9ee75b8502bc58c2f78c22974af71866',
	  appId : '132705266746978',
		status : true, // check login status
	    cookie : true, // enable cookies to allow the server to access the session
	    xfbml  : true  // parse XFBML
  });

  // fetch the status on load
  FB.getLoginStatus(handleSessionResponse);

  $('#login').bind('click', function() {
    FB.login(handleSessionResponse);
  });

  $('#logout').bind('click', function() {
    FB.logout(handleSessionResponse);
  });

  $('#disconnect').bind('click', function() {
    FB.api({ method: 'Auth.revokeAuthorization' }, function(response) {
      clearDisplay();
    });
  });

  // no user, clear display
  function clearDisplay() {
    $('#user-info').hide('fast');
  }

  // handle a session response from any of the auth related calls
  function handleSessionResponse(response) {
    // if we dont have a session, just hide the user info
    if (!response.session) {
      clearDisplay();
      return;
    }

    // if we have a session, query for the user's profile picture and name
    FB.api(
      {
        method: 'fql.query',
        query: 'SELECT name, pic FROM profile WHERE id=' + FB.getSession().uid
      },
      function(response) {
        var user = response[0];
        $('#user-info').html('<img src="' + user.pic + '">' + user.name).show('fast');
      }
    );
  }
  
  var centerRegionId = 'centerRegionId';
  
  Ext.onReady(function() {
	  new Ext.Viewport({
		  layout : 'border',
		  items : [
	           {
	        	   id : 'centerRegionId',
	        	   autoScroll : true,
	        	   region : 'center',
	        	   xtype : 'tabpanel',
	        	   activeTab : 0,
	        	   items : [
        	           new CC.Task.TaskList(),
        	           CC.Facebook.Test(),
        	           new CC.Task.TasksByOrg() 
//        	           new Ext.form.FormPanel({
//        	        	   title : 'Super Box Select Panel',
//        	        	   items : [
//								new Ext.ux.form.SuperBoxSelect({
//									   fieldLabel : 'Skills',
//									   store : new Ext.data.SimpleStore({
//										   fields : ['skillId', 'skillName'],
//										   data : [
//									           { skillId : '1', skillName : 'French' },
//									           { skillId : '2', skillName : 'Italian' },
//									           { skillId : '3', skillName : 'English' },
//									           { skillId : '4', skillName : 'Russian' },
//									           { skillId : '5', skillName : 'Spanish' }
//								        ]
//									   }),
//									   displayField : 'skillName',
//									   valueField : 'skillId'
//								})
//	        	           ]
//        	           }
        	           
	        	   ]
	           }
           ]
	           
	  });
  });