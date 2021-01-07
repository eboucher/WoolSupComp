# Selector for Product price currency:
PRODUCT_PRICE_CURRENCY_SELECTOR = '//div[contains(@class, "shopholder")]//*[@id="ContentPlaceHolder1_pnlPDetailBuyHolder"]//div[contains(@class, "buy-price")]//span[@class="product-price"]//span[@class="product-price-currency"]//text()'

# Selector for Product price amount:
PRODUCT_PRICE_AMOUNT_SELECTOR = '//div[contains(@class, "shopholder")]//*[@id="ContentPlaceHolder1_pnlPDetailBuyHolder"]//div[contains(@class, "buy-price")]//span[@class="product-price"]//span[@class="product-price-amount"]//text()'

# Selector for needle size:
NEEDLE_SIZE_SELECTOR = '//div[contains(@class, "shopholder")]//*[@id="ContentPlaceHolder1_pnShortSpecs"]//div[contains(@class, "innerspecsholder")]//*[@id="pdetailTableSpecs"]//table//tr[td//text()[contains(., "Nadelstärke")]]//td[2]//text()'

# Selector for Composition:
WOOL_COMPOSITION_SELECTOR = '//div[contains(@class, "shopholder")]//*[@id="ContentPlaceHolder1_pnShortSpecs"]//div[contains(@class, "innerspecsholder")]//*[@id="pdetailTableSpecs"]//table//tr[td//text()[contains(., "Zusammenstellung")]]//td[2]//text()'
