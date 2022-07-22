const puppeteer = require('puppeteer');

// describe('', ()=>{

//     let browser
//     let page
//     beforeAll( async ()=>{
//         browser = await puppeteer.launch({
//             headless: false,
//         })
//         page = await browser.newPage()
//         await page.goto('http://localhost:3000')
//     })

//     afterAll( (done)=>{
//         browser.close()
//         done()
//     })

//     describe('the homepage', () =>{

//         it('should render articles', async ()=>{
//             await page.waitForSelector('.odd-item')
//             let link = await page.$('.odd-item a')


//             // link.evaluate does not run code locally, it runs it in the puppeteer browser!
//             let linkText = await link.evaluate((linkEl)=> linkEl.innerText)
//             console.log('link text? ', linkText)
//             expect(linkText).toBe("Show HN: Warp, a Rust-based terminal")
//         })
//     })
// })

describe('', ()=>{

    let browser
    let page
    beforeAll( async ()=>{
        browser = await puppeteer.launch({
            headless: false,
        })
        page = await browser.newPage()
        await page.goto('http://localhost:3000')
    })

    afterAll( (done)=>{
        browser.close()
        done()
    })

    describe('the homepage', () =>{

        it('should render articles when a nav link is clicked', async ()=>{ 
            await page.waitForSelector('.navbar-nav')
            await page.click('.navbar-nav a')
            await page.waitForSelector('.title')
            
            const nextLink = await page.$('.even-item a')

            let nextLinkText = await nextLink.evaluate((linkEl)=> linkEl.innerText)
            
            console.log('next link text? ', nextLinkText)
            
            expect(nextLinkText).toBe("Show HN: An Attack on Titan Experience Made with ThreeJS")
        })
    })
})

