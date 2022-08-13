import { expect, it, describe, beforeAll, aferAll, afterAll } from 'vitest'
const puppeteer = require('puppeteer');

describe('the application', () => {
    let browser
    let page

    beforeAll(async () => {
        console.log('beforeAll() running')

        const configSettings = {
            // set headless false if you want to see a browser window for tests
            // otherwise set true
            headless: false,

            // slowMo runs puppeteer in slow-mode. Slows it down by the specified number of milliseconds.
            // Use it in conjunction with headless: false so you can watch the tests run in the browser.
            // Otherwise do not set this property on the config object at all
            slowMo: 500,

            // IMPORTANT: specific to mac you may not need this
            // IMPORTANT: On mac may have to do `brew install chromium` in the terminal/command line
            // On a mac you may have to install chromium as a separate step with a tool like homebrew
            // If so, use this option to tell puppeteer the path to the chromium binary/executable
            // (you can find this by running `which chromium` on the command line)
            // If you have not manually installed chromium & are not getting errors,
            // you do not need to set this property on the config object.
            executablePath: '/opt/homebrew/bin/chromium',
	    
            // If headless is true, this will also open devtools in the browser
            devTools: true,
        }

        browser = await puppeteer.launch(configSettings)
        console.log('browser open')
        page = await browser.newPage()
    })

    afterAll(async () => {
        await browser.close()
    })

    describe('homepage', () => {
        it("should welcome the user", async ()=>{
            console.log("test start")

            await page.goto("http://localhost:5173")
            await page.waitForSelector("#welcome")

            console.log("selector loaded")

            const welcomeElement = await page.$('#welcome')
            const welcomeText = await welcomeElement.evaluate((el)=> el.innerText)

            console.log(welcomeText)

            expect(welcomeText.includes('Welcome')).toBe(true)
            // Another way of doing the above
            //expect(welcomeText).toBe('Welcome')
        })
    })
})
