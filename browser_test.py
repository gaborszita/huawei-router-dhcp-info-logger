import asyncio
from typing import List
from pyppeteer import launch

USERNAME = "username"
PASSWORD = "password"

async def main() -> List:
    ip_info = []
    browser = await launch()
    page = await browser.newPage()
    await page.goto("http://192.168.0.1")
    # login
    await page.type("#txt_Username", USERNAME)
    await page.type("#txt_Password", PASSWORD)
    await page.keyboard.press("Enter")
    await page.waitForNavigation()
    await page.waitForSelector('li[name="subli_dhcpinfo"]')
    # dhcp info
    await page.click('li[name="subli_dhcpinfo"]')
    await page.waitForSelector("#frameContent")
    frame = page.frames[1]
    await frame.waitForSelector("#dhcpinfodat")
    await frame.waitForXPath('//*[contains(@class, "tabal_01")]/td[text() != "--"]')
    # get data and add it to the ip_info array
    rows = await frame.JJ(".tabal_01")
    for row in rows:
        row = await row.JJeval("td", "(nodes => nodes.map(n => n.innerText))")
        row_data = []
        for i in range(len(row)):
            if i==len(row)-1:
                data = row[i].replace(u"\xa0", " ")
                row_data.append(data)
            else:
                data = row[i][:-1].replace(u"\xa0", " ")
                row_data.append(data)
        ip_info.append(row_data)
    # logout
    await page.click("#headerLogoutText")
    await page.waitForNavigation()
    # await page.screenshot({'path': 'example.png'})
    await browser.close()
    return ip_info

ip_info = asyncio.get_event_loop().run_until_complete(main())
for row in ip_info:
    print(row)