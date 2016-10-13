var config = require("config.json")
casper.options.viewportSize={width: 1980, height: 1200}

casper.test.begin('Can configure hypervisor and add a profile',  function(test) {
  casper.start(config.baseurl);

// the login page
casper.then(function() {
    casper.test.assertExists("div#login-form")
    casper.test.assertTextExists("User name")
    casper.test.assertTextExists("Password")
    this.fillSelectors('div#login-form', {
        'input#login-user-input':     config.username,
        'input#login-password-input': config.password 
    }, true)
    
    if (config.make_screenshots) {this.capture("0_login.png")}
    
    this.click('#login-button')   
  })

// click the tools button 
casper.waitUntilVisible("#tools-menu > div > div.panel-heading > h4 > a",function() {
  casper.test.assertTextExists("Tools")
  casper.test.assertTextExists("Fleet Commander")
  if (config.make_screenshots) {this.capture("1_default_screen.png")}
  this.click("#tools-menu > div > div.panel-heading > h4 > a")
})


/*
casper.waitUntilVisible("a[href='/fleet-commander-admin']",function() {
  if (config.make_screenshots) {this.capture("2_click_expanded.png")}
  this.click('a[href="/fleet-commander-admin"]')   
});
*/


// casperjs barely supports iframes, load the fleet commander plugin window directly
casper.thenOpen(config.baseurl + '/cockpit/@localhost/fleet-commander-admin/index.html')

// fill in the settings and click install public key button
casper.waitUntilVisible("div#hypervisor-config-modal",function() {

  casper.test.assertExists('div#hypervisor-config-modal')
  casper.test.assertExists('button#show-pubkey-install')
  casper.test.assertExists('input#host')

  this.fillSelectors('div#hypervisor-config-modal', {
    'input#host':     config.libvirt_host,
    'input#username': config.username 
  }, true)

  this.click("button#show-pubkey-install")
});

// fill in the password
casper.waitUntilVisible("button#install-pubkey",function() {
  this.fillSelectors('body', {
    'input#pubkey-install-password':     config.password,
  }, true)
    
  this.click("button#install-pubkey"); 
  this.wait(1000)
})

// close the resulting window and save the settings
casper.then(function() {
  if (config.make_screenshots) {this.capture("4.png")}
  this.clickLabel('Close', 'button');
  this.clickLabel('Save', 'button');
})

casper.waitUntilVisible("#show-add-profile",function() {
  if (config.make_screenshots) {this.capture("5.png")}
})

casper.run(function() {test.done();});

});
