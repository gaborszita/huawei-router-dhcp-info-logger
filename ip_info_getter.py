import asyncio
from typing import List
from pyppeteer import launch
import config

# This file contains the main driver to get IP info from the router

class IpInfoGetter:
    async def __get_ip_info_router_comm() -> List:
        ip_info = []
        browser = await launch()
        page = await browser.newPage()
        await page.goto("http://192.168.0.1")
        # login
        await page.type("#txt_Username", config.ROUTER_USERNAME)
        await page.type("#txt_Password", config.ROUTER_PASSWORD)
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

    # get_ip_info() returns an array of arrays. Format of the smaller arrays 
    # in the big array:
    # - Host Name
    # - IP Address
    # - MAC address
    # - Remaining Lease Time
    # - Device Type (dhcp client)
    def get_ip_info() -> List:
        return asyncio.get_event_loop().run_until_complete(IpInfoGetter.__get_ip_info_router_comm())