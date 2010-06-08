/*
 * --------------------------------------------------------------------------
 * CrisisCorps.org
 * Copyright (c) 2010
 *
 * CrisisCorps is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * CrisisCorps is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with CrisisCorps.  If not, see <http://www.gnu.org/licenses/>.
 * --------------------------------------------------------------------------
 * 
 * File:   FacebookInteraction.js
 * Author: Alex Schoof <alex.schoof@gmail.com>
 * Major Revisions:
 *  
 * --------------------------------------------------------------------------
 */

Ext.namespace("CC.Facebook");

CC.Facebook.Test = function() {
	return {
	    title : 'Facebook Interaction',
	    height : 60,
	    layout : 'column',
	    defaults : {
		    columnWidth : 0.5
	    },
	    items : [
	        new Ext.Button({
	        	text : 'Load Friends',
	        	handler : function() {
	        		FB.api('/me/friends', function(response){
	        			Ext.Msg.alert("Status", "Loading "+response.data.length+" friends...");
	        			var jsonFriends = response.data;
	        			var center = Ext.getCmp('centerRegionId');
	        			if(center != null) {
	            			for(var i=0; i < jsonFriends.length; i++) {
	            				center.add(new Ext.Button({
	            					text : jsonFriends[i].name + " (" + jsonFriends[i].id + ")"
	            				}));
	                            //	        	            				if(i > 10) {
	                            //	        	            					break;
	                            //	        	            				}
	            			}
	        			}
	        			center.doLayout();
	        			
	        		});
	            }
	        }),
	        new Ext.Button({
	        	text : 'Do Some Crazy Sh*t',
	        	handler : function() {
	            	FB.ui(
	    			    {
	    			        method: 'stream.publish',
	    			        message: 'Having some fun at Random Hacks of Kindness!',
	    			        attachment: {
	    			            name: 'Connect',
	    			            caption: 'The Facebook Connect JavaScript SDK',
	    			            description: (
	    			                'A small JavaScript library that allows you to harness ' +
	    			                    'the power of Facebook, bringing the user\'s identity, ' +
	    			                    'social graph and distribution power to your site.'
	    			            ),
	    			            href: 'http://github.com/facebook/connect-js'
	    			        },
	    			        action_links: [
	    			            { text: 'Code', href: 'http://github.com/facebook/connect-js' }
	    			        ],
	    			        user_message_prompt: 'Share your thoughts about Connect'
	    			    },
	    			    function(response) {
	    			        if (response && response.post_id) {
	    			            alert('Post was published.');
	    			        } else {
	    			            alert('Post was not published.');
	    			        }
	    			    }
	    			);
	            }
	        })
	    ]
	};
}