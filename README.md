<div align="left">

[![Visit Peach payments](./header.png)](https://www.peachpayments.com&#x2F;)

# Peach payments<a id="peach-payments"></a>

The Payments API enables you to do a custom integration with Peach Payments and thereby support multiple payment methods.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`peachpayments.batch.generate_link`](#peachpaymentsbatchgenerate_link)
  * [`peachpayments.batch.get_batch_statuses`](#peachpaymentsbatchget_batch_statuses)
  * [`peachpayments.batch.get_error_files`](#peachpaymentsbatchget_error_files)
  * [`peachpayments.batch.link_status_get`](#peachpaymentsbatchlink_status_get)
  * [`peachpayments.checkout_v2_generation.initiate_checkout_instance`](#peachpaymentscheckout_v2_generationinitiate_checkout_instance)
  * [`peachpayments.checkout_generation.initiate_payment`](#peachpaymentscheckout_generationinitiate_payment)
  * [`peachpayments.checkout_generation.initiate_redirect_checkout`](#peachpaymentscheckout_generationinitiate_redirect_checkout)
  * [`peachpayments.checkout_generation.validate_request`](#peachpaymentscheckout_generationvalidate_request)
  * [`peachpayments.files.download_file`](#peachpaymentsfilesdownload_file)
  * [`peachpayments.files.upload_file`](#peachpaymentsfilesupload_file)
  * [`peachpayments.helpers.get_payment_methods`](#peachpaymentshelpersget_payment_methods)
  * [`peachpayments.payment.cancel_link`](#peachpaymentspaymentcancel_link)
  * [`peachpayments.payment.generate_link`](#peachpaymentspaymentgenerate_link)
  * [`peachpayments.payment.get_all_payment_links`](#peachpaymentspaymentget_all_payment_links)
  * [`peachpayments.payments_api_inbound.initiate_debit_transaction`](#peachpaymentspayments_api_inboundinitiate_debit_transaction)
  * [`peachpayments.payments_api_inbound.query_transaction_by_id`](#peachpaymentspayments_api_inboundquery_transaction_by_id)
  * [`peachpayments.payments_api_inbound.refund_transaction`](#peachpaymentspayments_api_inboundrefund_transaction)
  * [`peachpayments.payments_api_inbound.status`](#peachpaymentspayments_api_inboundstatus)
  * [`peachpayments.payments_api_outbound.webhook`](#peachpaymentspayments_api_outboundwebhook)
  * [`peachpayments.status.checkout_status_get`](#peachpaymentsstatuscheckout_status_get)
  * [`peachpayments.status.query_payment_status`](#peachpaymentsstatusquery_payment_status)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Peach%20Payments&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from peach_payments_python_sdk import PeachPayments, ApiException

peachpayments = PeachPayments(access_token="YOUR_BEARER_TOKEN")

try:
    # Generate batch link
    generate_link_response = peachpayments.batch.generate_link(
        filename="test.csv",
        entity_id="8ac7a4ca694cec2601694cf5f9360026",
        notification_url="https://webhook.site/",
    )
    print(generate_link_response)
except ApiException as e:
    print("Exception when calling BatchApi.generate_link: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["message"])
    if e.status == 401:
        pprint(e.body["message"])
    if e.status == 404:
        pprint(e.body["message"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from peach_payments_python_sdk import PeachPayments, ApiException

peachpayments = PeachPayments(access_token="YOUR_BEARER_TOKEN")


async def main():
    try:
        # Generate batch link
        generate_link_response = await peachpayments.batch.agenerate_link(
            filename="test.csv",
            entity_id="8ac7a4ca694cec2601694cf5f9360026",
            notification_url="https://webhook.site/",
        )
        print(generate_link_response)
    except ApiException as e:
        print("Exception when calling BatchApi.generate_link: %s\n" % e)
        pprint(e.body)
        if e.status == 400:
            pprint(e.body["message"])
        if e.status == 401:
            pprint(e.body["message"])
        if e.status == 404:
            pprint(e.body["message"])
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from peach_payments_python_sdk import PeachPayments, ApiException

peachpayments = PeachPayments(access_token="YOUR_BEARER_TOKEN")

try:
    # Generate batch link
    generate_link_response = peachpayments.batch.raw.generate_link(
        filename="test.csv",
        entity_id="8ac7a4ca694cec2601694cf5f9360026",
        notification_url="https://webhook.site/",
    )
    pprint(generate_link_response.body)
    pprint(generate_link_response.body["id"])
    pprint(generate_link_response.body["url"])
    pprint(generate_link_response.headers)
    pprint(generate_link_response.status)
    pprint(generate_link_response.round_trip_time)
except ApiException as e:
    print("Exception when calling BatchApi.generate_link: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["message"])
    if e.status == 401:
        pprint(e.body["message"])
    if e.status == 404:
        pprint(e.body["message"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `peachpayments.batch.generate_link`<a id="peachpaymentsbatchgenerate_link"></a>

Returns a URL to which the batch file must be uploaded.

For more information, see the [documentation](https://developer.peachpayments.com/docs/generate-bulk-payment-links).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_link_response = peachpayments.batch.generate_link(
    filename="test.csv",
    entity_id="8ac7a4ca694cec2601694cf5f9360026",
    notification_url="https://webhook.site/",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### filename: `str`<a id="filename-str"></a>

The name of the CSV to be uploaded.

##### entity_id: `str`<a id="entity_id-str"></a>

The entity for the request.

##### notification_url: `Optional[str]`<a id="notification_url-optionalstr"></a>

Webhooks are sent to this URL. It overrides the generic merchant webhook URL.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BatchGenerateLinkRequest`](./peach_payments_python_sdk/type/batch_generate_link_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BatchGenerateLinkResponse`](./peach_payments_python_sdk/pydantic/batch_generate_link_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/channels/{entityId}/payments/batches` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peachpayments.batch.get_batch_statuses`<a id="peachpaymentsbatchget_batch_statuses"></a>

Query all batch statuses of a batch for a channel.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_batch_statuses_response = peachpayments.batch.get_batch_statuses(
    entity_id="8ac7a4ca694cec2601694cf5f9360026",
    offset=0,
    per_page=50,
    filters_start_date="2018-03-20T09:12:28Z",
    filters_end_date="2018-03-20T09:12:28Z",
    filters_status="initiated",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### entity_id: `str`<a id="entity_id-str"></a>

The entity for the request.

##### offset: `Union[int, float]`<a id="offset-unionint-float"></a>

The offset from which to read data.

##### per_page: `Union[int, float]`<a id="per_page-unionint-float"></a>

The amount of items to retrieve.

##### filters_start_date: `datetime`<a id="filters_start_date-datetime"></a>

Retrieve all batches from the start date onwards.

##### filters_end_date: `datetime`<a id="filters_end_date-datetime"></a>

Retrieve all batches until the end date.

##### filters_status: `str`<a id="filters_status-str"></a>

The payment link status to filter on.

#### 🔄 Return<a id="🔄-return"></a>

[`BatchGetBatchStatusesResponse`](./peach_payments_python_sdk/pydantic/batch_get_batch_statuses_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/channels/{entityId}/payments/batches` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peachpayments.batch.get_error_files`<a id="peachpaymentsbatchget_error_files"></a>

Returns a set of URLs that can be accessed to retrieve the batch error files.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_error_files_response = peachpayments.batch.get_error_files(
    batch_id="421e1e63-ddd5-46ec-8812-74eda861259b",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### batch_id: `str`<a id="batch_id-str"></a>

The batch for the request.

#### 🔄 Return<a id="🔄-return"></a>

[`BatchGetErrorFilesResponse`](./peach_payments_python_sdk/pydantic/batch_get_error_files_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/batches/{batchId}/files` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peachpayments.batch.link_status_get`<a id="peachpaymentsbatchlink_status_get"></a>

Returns the status of the batch.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
link_status_get_response = peachpayments.batch.link_status_get(
    batch_id="421e1e63-ddd5-46ec-8812-74eda861259b",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### batch_id: `str`<a id="batch_id-str"></a>

The batch ID for the request.

#### 🔄 Return<a id="🔄-return"></a>

[`BatchResponse`](./peach_payments_python_sdk/pydantic/batch_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/batches/{batchId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peachpayments.checkout_v2_generation.initiate_checkout_instance`<a id="peachpaymentscheckout_v2_generationinitiate_checkout_instance"></a>

Create a checkout instance for use from Embedded Checkout.

For more information, see the [documentation](https://developer.peachpayments.com/docs/checkout-embedded-tutorial#tutorial). 


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
initiate_checkout_instance_response = (
    peachpayments.checkout_v2_generation.initiate_checkout_instance(
        authentication_entity_id="8ac7a4ca68c22c4d0168c2caab2e0025",
        merchant_transaction_id="OrderNo453432",
        amount=1010.22,
        currency="ZAR",
        nonce="UNQ00012345678",
        shopper_result_url="https://mydemostore.com/OrderNo453432",
        referer="https://mydemostore.com",
        default_payment_method="CARD",
        force_default_method=True,
        merchant_invoice_id="INV-00001",
        cancel_url="https://mydemostore.com/OrderNo453432/cancelled",
        notification_url="https://mydemostore.com/OrderNo453432/webhook",
        custom_parameters={
            "key": "",
        },
        customer={
            "merchant_customer_id": "971020",
            "given_name": "John",
            "surname": "Smith",
            "mobile": "27123456789",
            "email": "johnsmith@mail.com",
            "id_number": "9001010000084",
        },
        billing={
            "street1": "1 Example Road",
            "street2": "LocalityA",
            "city": "Cape Town",
            "company": "CompanyA",
            "country": "ZA",
            "state": "Western Cape",
            "postcode": "1234",
        },
        shipping={
            "street1": "1 Example Road",
            "street2": "LocalityA",
            "city": "Cape Town",
            "company": "CompanyA",
            "postcode": "1234",
            "country": "ZA",
            "state": "Western Cape",
        },
        create_registration=True,
        originator="Webstore",
        return_to="STORE",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authentication_entity_id: `str`<a id="authentication_entity_id-str"></a>

The entity for the request. By default, this is the channel ID.

##### merchant_transaction_id: `str`<a id="merchant_transaction_id-str"></a>

Merchant-provided reference number unique for your transactions.

##### amount: `Union[int, float]`<a id="amount-unionint-float"></a>

The amount of the payment request. The period is used as the decimal separator.  M-PESA does not support decimal amounts, so Checkout automatically rounds them up. 

##### currency: `str`<a id="currency-str"></a>

The currency code of the payment request amount.

##### nonce: `str`<a id="nonce-str"></a>

Unique value to represent each request.

##### shopper_result_url: `str`<a id="shopper_result_url-str"></a>

Checkout uses a POST request to redirect the customer to this URL after the customer completes checkout. Must be a valid URL that can be accessed through a browser.

##### referer: `str`<a id="referer-str"></a>

An allowlisted domain for the merchant.

##### default_payment_method: `str`<a id="default_payment_method-str"></a>

The preferred payment method which is active in the checkout page at the point of redirecting.

##### force_default_method: `bool`<a id="force_default_method-bool"></a>

Force the default payment method to be the only payment method.

##### merchant_invoice_id: `str`<a id="merchant_invoice_id-str"></a>

Merchant-provided invoice number unique for your transactions. This identifier is not sent onwards.

##### cancel_url: `str`<a id="cancel_url-str"></a>

The customer is redirected to this URL if they cancel checkout. It must be a valid URL that can be reached through a browser.

##### notification_url: `str`<a id="notification_url-str"></a>

Override the preconfigured webhook URL for this checkout instance, any changes to checkout send a webhook to this URL.

##### custom_parameters: [`CheckoutV2CustomParameters`](./peach_payments_python_sdk/type/checkout_v2_custom_parameters.py)<a id="custom_parameters-checkoutv2customparameterspeach_payments_python_sdktypecheckout_v2_custom_parameterspy"></a>

##### customer: [`CheckoutV2Customer`](./peach_payments_python_sdk/type/checkout_v2_customer.py)<a id="customer-checkoutv2customerpeach_payments_python_sdktypecheckout_v2_customerpy"></a>


##### billing: [`CheckoutV2Billing`](./peach_payments_python_sdk/type/checkout_v2_billing.py)<a id="billing-checkoutv2billingpeach_payments_python_sdktypecheckout_v2_billingpy"></a>


##### shipping: [`CheckoutV2Shipping`](./peach_payments_python_sdk/type/checkout_v2_shipping.py)<a id="shipping-checkoutv2shippingpeach_payments_python_sdktypecheckout_v2_shippingpy"></a>


##### create_registration: `bool`<a id="create_registration-bool"></a>

Used to enable card tokenisation with COPYandPAY.

##### originator: `str`<a id="originator-str"></a>

Used to provide a name for the application that is creating the checkout instance.

##### return_to: `str`<a id="return_to-str"></a>

Text to display on \\\"Return to Store\\\" button on completing checkout.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CheckoutV2`](./peach_payments_python_sdk/type/checkout_v2.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CheckoutV2GenerationInitiateCheckoutInstanceResponse`](./peach_payments_python_sdk/pydantic/checkout_v2_generation_initiate_checkout_instance_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/checkout` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peachpayments.checkout_generation.initiate_payment`<a id="peachpaymentscheckout_generationinitiate_payment"></a>

Load the Checkout frontend to complete a payment. The POST request contains the entityId, signature, purchase parameters, and any custom parameters that a merchant optionally sends.

Sign the data on the backend and execute the POST from the browser.

For more information, see the [documentation](https://developer.peachpayments.com/docs/checkout-payment#form-post-checkout).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
initiate_payment_response = peachpayments.checkout_generation.initiate_payment(
    referer="https://mydemostore.com",
    authentication_entity_id="8ac7a4ca68c22c4d0168c2caab2e0025",
    signature="a668342244a9c77b08a2f9090d033d6e2610b431a5c0ca975f32035ed06164f4",
    merchant_transaction_id="OrderNo453432",
    amount="1010.22",
    payment_type="DB",
    currency="ZAR",
    nonce="UNQ00012345678",
    shopper_result_url="https://mydemostore.com/OrderNo453432",
    default_payment_method="CARD",
    force_default_method="false",
    merchant_invoice_id="INV-0001",
    cancel_url="https://mydemostore.com/OrderNo453432/cancelled",
    notification_url="https://mydemostore.com/OrderNo453432/webhook",
    custom_parameters_name="name: Name1 value: Value1",
    customer_merchant_customer_id="971020",
    customer_given_name="John",
    customer_surname="Smith",
    customer_mobile="27123456789",
    customer_email="johnsmith@mail.com",
    customer_status="EXISTING",
    customer_birth_date="1970-02-17",
    customer_ip="192.168.1.1",
    customer_phone="27123456789",
    customer_id_number="9001010000084",
    billing_street1="1 Example Road",
    billing_street2="LocalityA",
    billing_city="Cape Town",
    billing_company="CompanyA",
    billing_country="ZA",
    billing_state="Western Cape",
    billing_postcode="1234",
    shipping_street1="1 Example Road",
    shipping_street2="LocalityA",
    shipping_city="Cape Town",
    shipping_company="CompanyA",
    shipping_postcode="1234",
    shipping_country="ZA",
    shipping_state="Western Cape",
    cart_tax="15.00",
    cart_shipping_amount="12.25",
    cart_discount="02.25",
    create_registration="false",
    originator="Webstore",
    return_to="STORE",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### referer: `str`<a id="referer-str"></a>

An allowlisted domain for the merchant.

##### authentication_entity_id: `str`<a id="authentication_entity_id-str"></a>

The entity for the request. By default, this is the channel ID.

##### signature: `str`<a id="signature-str"></a>

Token to verify the integrity of the payment, ensuring that only the merchant sending the request is accepted.

##### merchant_transaction_id: `str`<a id="merchant_transaction_id-str"></a>

Merchant-provided reference number unique for your transactions.

##### amount: `str`<a id="amount-str"></a>

The amount of the payment request. The period is used as the decimal separator. M-PESA does not support decimal amounts, so Checkout automatically rounds them up.

##### payment_type: `str`<a id="payment_type-str"></a>

The payment type for the request. Accepts `DB`.  Does not accept `RG`, but you can tokenise a card by performing a DB with `createRegistration`.  Refund transactions through the Dashboard or as described in the <a href=\\\"https://developer.peachpayments.com/docs/checkout-refund\\\" target=\\\"_blank\\\">documentation</a>. 

##### currency: `str`<a id="currency-str"></a>

The currency code of the payment request amount.

##### nonce: `str`<a id="nonce-str"></a>

Unique value to represent each request.

##### shopper_result_url: `str`<a id="shopper_result_url-str"></a>

Checkout uses a POST request to redirect the customer to this URL after the customer completes checkout. Must be a valid URL that can be accessed through a browser.

##### default_payment_method: `str`<a id="default_payment_method-str"></a>

The preferred payment method which is active in the checkout page at the point of redirecting.

##### force_default_method: `str`<a id="force_default_method-str"></a>

Force the default payment method to be the only payment method.

##### merchant_invoice_id: `str`<a id="merchant_invoice_id-str"></a>

Merchant-provided invoice number unique for your transactions. This identifier is not sent onwards.

##### cancel_url: `str`<a id="cancel_url-str"></a>

The customer is redirected to this URL if they cancel checkout. It must be a valid URL that can be reached through a browser.

##### notification_url: `str`<a id="notification_url-str"></a>

Override the preconfigured webhook URL for this checkout instance, any changes to checkout will send a webhook to this url.

##### custom_parameters_name: `str`<a id="custom_parameters_name-str"></a>

A name value pair used for sending custom information.

##### customer_merchant_customer_id: `str`<a id="customer_merchant_customer_id-str"></a>

An identifier for this customer. Typically this is the ID that identifies the shopper in the shop's system.

##### customer_given_name: `str`<a id="customer_given_name-str"></a>

The customer's first name or given name.  Required if you send in any other customer parameters, and for some risk checks and payment providers.  Peach Payments recommends including the name so that it displays in the Peach Dashboard and is available for subsequent queries.  Truncated after 48 characters. 

##### customer_surname: `str`<a id="customer_surname-str"></a>

The customer's last name or surname.  Required if you send in any other customer parameters, and for some risk checks and payment providers.  Peach Payments recommends including the surname so that it displays in the Peach Dashboard and is available for subsequent queries.  Truncated after 48 characters. 

##### customer_mobile: `str`<a id="customer_mobile-str"></a>

The customer's mobile number.

##### customer_email: `str`<a id="customer_email-str"></a>

The customer's email address.

##### customer_status: `str`<a id="customer_status-str"></a>

The customer's status. Accepts `NEW` or `EXISTING`.

##### customer_birth_date: `str`<a id="customer_birth_date-str"></a>

The customer's birth date in the yyyy-MM-dd format.

##### customer_ip: `str`<a id="customer_ip-str"></a>

The customer's IP address.

##### customer_phone: `str`<a id="customer_phone-str"></a>

The customer's phone number.

##### customer_id_number: `str`<a id="customer_id_number-str"></a>

The customer's ID number, required for high-risk merchants supporting Capitec Pay.

##### billing_street1: `str`<a id="billing_street1-str"></a>

The door number, floor, building number, building name, and/or street name of the billing address.

##### billing_street2: `str`<a id="billing_street2-str"></a>

The adjoining road or locality, if required, of the billing address.

##### billing_city: `str`<a id="billing_city-str"></a>

The town, district, or city of the billing address.

##### billing_company: `str`<a id="billing_company-str"></a>

The company of the billing address.

##### billing_country: `str`<a id="billing_country-str"></a>

The country of the billing address (ISO 3166-1).

##### billing_state: `str`<a id="billing_state-str"></a>

The county, state, or region of the billing address.

##### billing_postcode: `str`<a id="billing_postcode-str"></a>

The postal code or ZIP code of the billing address.

##### shipping_street1: `str`<a id="shipping_street1-str"></a>

The door number, floor, building number, building name, and/or street name of the shipping address.

##### shipping_street2: `str`<a id="shipping_street2-str"></a>

The adjoining road or locality, if required, of the shipping address.

##### shipping_city: `str`<a id="shipping_city-str"></a>

The town, district, or city of the shipping address.

##### shipping_company: `str`<a id="shipping_company-str"></a>

The company of the shipping address.

##### shipping_postcode: `str`<a id="shipping_postcode-str"></a>

The postal code or ZIP code of the shipping address.

##### shipping_country: `str`<a id="shipping_country-str"></a>

The country of the shipping address (ISO 3166-1).

##### shipping_state: `str`<a id="shipping_state-str"></a>

The county, state, or region of the shipping address.

##### cart_tax: `str`<a id="cart_tax-str"></a>

The tax percentage applied to the price of the item in the shopping cart.

##### cart_shipping_amount: `str`<a id="cart_shipping_amount-str"></a>

The total amount of the cart item including quantity.

##### cart_discount: `str`<a id="cart_discount-str"></a>

Discount amount applied on order amount.

##### create_registration: `str`<a id="create_registration-str"></a>

Used to enable card tokenisation with COPYandPAY.

##### originator: `str`<a id="originator-str"></a>

Used to provide a name for the application that is creating the checkout instance.

##### return_to: `str`<a id="return_to-str"></a>

Text to display on \\\"Return to Store\\\" button on completing checkout.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Checkout`](./peach_payments_python_sdk/type/checkout.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/checkout` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peachpayments.checkout_generation.initiate_redirect_checkout`<a id="peachpaymentscheckout_generationinitiate_redirect_checkout"></a>

Provide a redirect URL to the caller to redirect the user into the Checkout experience. The POST request contains the entityId, signature, purchase parameters, and any custom parameters that a merchant optionally sends. This allows the checkout instance to be created from a backend without requiring a "form post", or other similar method, from the frontend.

For more information, see the [documentation](https://developer.peachpayments.com/docs/checkout-payment#redirect-based-checkout).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
initiate_redirect_checkout_response = (
    peachpayments.checkout_generation.initiate_redirect_checkout(
        authentication_entity_id="8ac7a4ca68c22c4d0168c2caab2e0025",
        signature="a668342244a9c77b08a2f9090d033d6e2610b431a5c0ca975f32035ed06164f4",
        merchant_transaction_id="OrderNo453432",
        amount="1010.22",
        payment_type="DB",
        currency="ZAR",
        nonce="UNQ00012345678",
        shopper_result_url="https://mydemostore.com/OrderNo453432",
        referer="https://mydemostore.com",
        default_payment_method="CARD",
        force_default_method="false",
        merchant_invoice_id="INV-0001",
        cancel_url="https://mydemostore.com/OrderNo453432/cancelled",
        notification_url="https://mydemostore.com/OrderNo453432/webhook",
        custom_parameters_name="name: Name1 value: Value1",
        customer_merchant_customer_id="971020",
        customer_given_name="John",
        customer_surname="Smith",
        customer_mobile="27123456789",
        customer_email="johnsmith@mail.com",
        customer_status="EXISTING",
        customer_birth_date="1970-02-17",
        customer_ip="192.168.1.1",
        customer_phone="27123456789",
        customer_id_number="9001010000084",
        billing_street1="1 Example Road",
        billing_street2="LocalityA",
        billing_city="Cape Town",
        billing_company="CompanyA",
        billing_country="ZA",
        billing_state="Western Cape",
        billing_postcode="1234",
        shipping_street1="1 Example Road",
        shipping_street2="LocalityA",
        shipping_city="Cape Town",
        shipping_company="CompanyA",
        shipping_postcode="1234",
        shipping_country="ZA",
        shipping_state="Western Cape",
        cart_tax="15.00",
        cart_shipping_amount="12.25",
        cart_discount="02.25",
        create_registration="false",
        originator="Webstore",
        return_to="STORE",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authentication_entity_id: `str`<a id="authentication_entity_id-str"></a>

The entity for the request. By default, this is the channel ID.

##### signature: `str`<a id="signature-str"></a>

Token to verify the integrity of the payment, ensuring that only the merchant sending the request is accepted.

##### merchant_transaction_id: `str`<a id="merchant_transaction_id-str"></a>

Merchant-provided reference number unique for your transactions.

##### amount: `str`<a id="amount-str"></a>

The amount of the payment request. The period is used as the decimal separator. M-PESA does not support decimal amounts, so Checkout automatically rounds them up.

##### payment_type: `str`<a id="payment_type-str"></a>

The payment type for the request. Accepts `DB`.  Does not accept `RG`, but you can tokenise a card by performing a DB with `createRegistration`.  Refund transactions through the Dashboard or as described in the <a href=\\\"https://developer.peachpayments.com/docs/checkout-refund\\\" target=\\\"_blank\\\">documentation</a>. 

##### currency: `str`<a id="currency-str"></a>

The currency code of the payment request amount.

##### nonce: `str`<a id="nonce-str"></a>

Unique value to represent each request.

##### shopper_result_url: `str`<a id="shopper_result_url-str"></a>

Checkout uses a POST request to redirect the customer to this URL after the customer completes checkout. Must be a valid URL that can be accessed through a browser.

##### referer: `str`<a id="referer-str"></a>

An allowlisted domain for the merchant.

##### default_payment_method: `str`<a id="default_payment_method-str"></a>

The preferred payment method which is active in the checkout page at the point of redirecting.

##### force_default_method: `str`<a id="force_default_method-str"></a>

Force the default payment method to be the only payment method.

##### merchant_invoice_id: `str`<a id="merchant_invoice_id-str"></a>

Merchant-provided invoice number unique for your transactions. This identifier is not sent onwards.

##### cancel_url: `str`<a id="cancel_url-str"></a>

The customer is redirected to this URL if they cancel checkout. It must be a valid URL that can be reached through a browser.

##### notification_url: `str`<a id="notification_url-str"></a>

Override the preconfigured webhook URL for this checkout instance, any changes to checkout will send a webhook to this url.

##### custom_parameters_name: `str`<a id="custom_parameters_name-str"></a>

A name value pair used for sending custom information.

##### customer_merchant_customer_id: `str`<a id="customer_merchant_customer_id-str"></a>

An identifier for this customer. Typically this is the ID that identifies the shopper in the shop's system.

##### customer_given_name: `str`<a id="customer_given_name-str"></a>

The customer's first name or given name.  Required if you send in any other customer parameters, and for some risk checks and payment providers.  Peach Payments recommends including the name so that it displays in the Peach Dashboard and is available for subsequent queries.  Truncated after 48 characters. 

##### customer_surname: `str`<a id="customer_surname-str"></a>

The customer's last name or surname.  Required if you send in any other customer parameters, and for some risk checks and payment providers.  Peach Payments recommends including the surname so that it displays in the Peach Dashboard and is available for subsequent queries.  Truncated after 48 characters. 

##### customer_mobile: `str`<a id="customer_mobile-str"></a>

The customer's mobile number.

##### customer_email: `str`<a id="customer_email-str"></a>

The customer's email address.

##### customer_status: `str`<a id="customer_status-str"></a>

The customer's status. Accepts `NEW` or `EXISTING`.

##### customer_birth_date: `str`<a id="customer_birth_date-str"></a>

The customer's birth date in the yyyy-MM-dd format.

##### customer_ip: `str`<a id="customer_ip-str"></a>

The customer's IP address.

##### customer_phone: `str`<a id="customer_phone-str"></a>

The customer's phone number.

##### customer_id_number: `str`<a id="customer_id_number-str"></a>

The customer's ID number, required for high-risk merchants supporting Capitec Pay.

##### billing_street1: `str`<a id="billing_street1-str"></a>

The door number, floor, building number, building name, and/or street name of the billing address.

##### billing_street2: `str`<a id="billing_street2-str"></a>

The adjoining road or locality, if required, of the billing address.

##### billing_city: `str`<a id="billing_city-str"></a>

The town, district, or city of the billing address.

##### billing_company: `str`<a id="billing_company-str"></a>

The company of the billing address.

##### billing_country: `str`<a id="billing_country-str"></a>

The country of the billing address (ISO 3166-1).

##### billing_state: `str`<a id="billing_state-str"></a>

The county, state, or region of the billing address.

##### billing_postcode: `str`<a id="billing_postcode-str"></a>

The postal code or ZIP code of the billing address.

##### shipping_street1: `str`<a id="shipping_street1-str"></a>

The door number, floor, building number, building name, and/or street name of the shipping address.

##### shipping_street2: `str`<a id="shipping_street2-str"></a>

The adjoining road or locality, if required, of the shipping address.

##### shipping_city: `str`<a id="shipping_city-str"></a>

The town, district, or city of the shipping address.

##### shipping_company: `str`<a id="shipping_company-str"></a>

The company of the shipping address.

##### shipping_postcode: `str`<a id="shipping_postcode-str"></a>

The postal code or ZIP code of the shipping address.

##### shipping_country: `str`<a id="shipping_country-str"></a>

The country of the shipping address (ISO 3166-1).

##### shipping_state: `str`<a id="shipping_state-str"></a>

The county, state, or region of the shipping address.

##### cart_tax: `str`<a id="cart_tax-str"></a>

The tax percentage applied to the price of the item in the shopping cart.

##### cart_shipping_amount: `str`<a id="cart_shipping_amount-str"></a>

The total amount of the cart item including quantity.

##### cart_discount: `str`<a id="cart_discount-str"></a>

Discount amount applied on order amount.

##### create_registration: `str`<a id="create_registration-str"></a>

Used to enable card tokenisation with COPYandPAY.

##### originator: `str`<a id="originator-str"></a>

Used to provide a name for the application that is creating the checkout instance.

##### return_to: `str`<a id="return_to-str"></a>

Text to display on \\\"Return to Store\\\" button on completing checkout.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Checkout`](./peach_payments_python_sdk/type/checkout.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CheckoutGenerationInitiateRedirectCheckoutResponse`](./peach_payments_python_sdk/pydantic/checkout_generation_initiate_redirect_checkout_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/checkout/initiate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peachpayments.checkout_generation.validate_request`<a id="peachpaymentscheckout_generationvalidate_request"></a>

Validate a request before trying to initiate a checkout session.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
validate_request_response = peachpayments.checkout_generation.validate_request(
    authentication_entity_id="8ac7a4ca68c22c4d0168c2caab2e0025",
    signature="a668342244a9c77b08a2f9090d033d6e2610b431a5c0ca975f32035ed06164f4",
    merchant_transaction_id="OrderNo453432",
    amount="1010.22",
    payment_type="DB",
    currency="ZAR",
    nonce="UNQ00012345678",
    shopper_result_url="https://mydemostore.com/OrderNo453432",
    referer="https://mydemostore.com",
    default_payment_method="CARD",
    force_default_method="false",
    merchant_invoice_id="INV-0001",
    cancel_url="https://mydemostore.com/OrderNo453432/cancelled",
    notification_url="https://mydemostore.com/OrderNo453432/webhook",
    custom_parameters_name="name: Name1 value: Value1",
    customer_merchant_customer_id="971020",
    customer_given_name="John",
    customer_surname="Smith",
    customer_mobile="27123456789",
    customer_email="johnsmith@mail.com",
    customer_status="EXISTING",
    customer_birth_date="1970-02-17",
    customer_ip="192.168.1.1",
    customer_phone="27123456789",
    customer_id_number="9001010000084",
    billing_street1="1 Example Road",
    billing_street2="LocalityA",
    billing_city="Cape Town",
    billing_company="CompanyA",
    billing_country="ZA",
    billing_state="Western Cape",
    billing_postcode="1234",
    shipping_street1="1 Example Road",
    shipping_street2="LocalityA",
    shipping_city="Cape Town",
    shipping_company="CompanyA",
    shipping_postcode="1234",
    shipping_country="ZA",
    shipping_state="Western Cape",
    cart_tax="15.00",
    cart_shipping_amount="12.25",
    cart_discount="02.25",
    create_registration="false",
    originator="Webstore",
    return_to="STORE",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authentication_entity_id: `str`<a id="authentication_entity_id-str"></a>

The entity for the request. By default, this is the channel ID.

##### signature: `str`<a id="signature-str"></a>

Token to verify the integrity of the payment, ensuring that only the merchant sending the request is accepted.

##### merchant_transaction_id: `str`<a id="merchant_transaction_id-str"></a>

Merchant-provided reference number unique for your transactions.

##### amount: `str`<a id="amount-str"></a>

The amount of the payment request. The period is used as the decimal separator. M-PESA does not support decimal amounts, so Checkout automatically rounds them up.

##### payment_type: `str`<a id="payment_type-str"></a>

The payment type for the request. Accepts `DB`.  Does not accept `RG`, but you can tokenise a card by performing a DB with `createRegistration`.  Refund transactions through the Dashboard or as described in the <a href=\\\"https://developer.peachpayments.com/docs/checkout-refund\\\" target=\\\"_blank\\\">documentation</a>. 

##### currency: `str`<a id="currency-str"></a>

The currency code of the payment request amount.

##### nonce: `str`<a id="nonce-str"></a>

Unique value to represent each request.

##### shopper_result_url: `str`<a id="shopper_result_url-str"></a>

Checkout uses a POST request to redirect the customer to this URL after the customer completes checkout. Must be a valid URL that can be accessed through a browser.

##### referer: `str`<a id="referer-str"></a>

An allowlisted domain for the merchant.

##### default_payment_method: `str`<a id="default_payment_method-str"></a>

The preferred payment method which is active in the checkout page at the point of redirecting.

##### force_default_method: `str`<a id="force_default_method-str"></a>

Force the default payment method to be the only payment method.

##### merchant_invoice_id: `str`<a id="merchant_invoice_id-str"></a>

Merchant-provided invoice number unique for your transactions. This identifier is not sent onwards.

##### cancel_url: `str`<a id="cancel_url-str"></a>

The customer is redirected to this URL if they cancel checkout. It must be a valid URL that can be reached through a browser.

##### notification_url: `str`<a id="notification_url-str"></a>

Override the preconfigured webhook URL for this checkout instance, any changes to checkout will send a webhook to this url.

##### custom_parameters_name: `str`<a id="custom_parameters_name-str"></a>

A name value pair used for sending custom information.

##### customer_merchant_customer_id: `str`<a id="customer_merchant_customer_id-str"></a>

An identifier for this customer. Typically this is the ID that identifies the shopper in the shop's system.

##### customer_given_name: `str`<a id="customer_given_name-str"></a>

The customer's first name or given name.  Required if you send in any other customer parameters, and for some risk checks and payment providers.  Peach Payments recommends including the name so that it displays in the Peach Dashboard and is available for subsequent queries.  Truncated after 48 characters. 

##### customer_surname: `str`<a id="customer_surname-str"></a>

The customer's last name or surname.  Required if you send in any other customer parameters, and for some risk checks and payment providers.  Peach Payments recommends including the surname so that it displays in the Peach Dashboard and is available for subsequent queries.  Truncated after 48 characters. 

##### customer_mobile: `str`<a id="customer_mobile-str"></a>

The customer's mobile number.

##### customer_email: `str`<a id="customer_email-str"></a>

The customer's email address.

##### customer_status: `str`<a id="customer_status-str"></a>

The customer's status. Accepts `NEW` or `EXISTING`.

##### customer_birth_date: `str`<a id="customer_birth_date-str"></a>

The customer's birth date in the yyyy-MM-dd format.

##### customer_ip: `str`<a id="customer_ip-str"></a>

The customer's IP address.

##### customer_phone: `str`<a id="customer_phone-str"></a>

The customer's phone number.

##### customer_id_number: `str`<a id="customer_id_number-str"></a>

The customer's ID number, required for high-risk merchants supporting Capitec Pay.

##### billing_street1: `str`<a id="billing_street1-str"></a>

The door number, floor, building number, building name, and/or street name of the billing address.

##### billing_street2: `str`<a id="billing_street2-str"></a>

The adjoining road or locality, if required, of the billing address.

##### billing_city: `str`<a id="billing_city-str"></a>

The town, district, or city of the billing address.

##### billing_company: `str`<a id="billing_company-str"></a>

The company of the billing address.

##### billing_country: `str`<a id="billing_country-str"></a>

The country of the billing address (ISO 3166-1).

##### billing_state: `str`<a id="billing_state-str"></a>

The county, state, or region of the billing address.

##### billing_postcode: `str`<a id="billing_postcode-str"></a>

The postal code or ZIP code of the billing address.

##### shipping_street1: `str`<a id="shipping_street1-str"></a>

The door number, floor, building number, building name, and/or street name of the shipping address.

##### shipping_street2: `str`<a id="shipping_street2-str"></a>

The adjoining road or locality, if required, of the shipping address.

##### shipping_city: `str`<a id="shipping_city-str"></a>

The town, district, or city of the shipping address.

##### shipping_company: `str`<a id="shipping_company-str"></a>

The company of the shipping address.

##### shipping_postcode: `str`<a id="shipping_postcode-str"></a>

The postal code or ZIP code of the shipping address.

##### shipping_country: `str`<a id="shipping_country-str"></a>

The country of the shipping address (ISO 3166-1).

##### shipping_state: `str`<a id="shipping_state-str"></a>

The county, state, or region of the shipping address.

##### cart_tax: `str`<a id="cart_tax-str"></a>

The tax percentage applied to the price of the item in the shopping cart.

##### cart_shipping_amount: `str`<a id="cart_shipping_amount-str"></a>

The total amount of the cart item including quantity.

##### cart_discount: `str`<a id="cart_discount-str"></a>

Discount amount applied on order amount.

##### create_registration: `str`<a id="create_registration-str"></a>

Used to enable card tokenisation with COPYandPAY.

##### originator: `str`<a id="originator-str"></a>

Used to provide a name for the application that is creating the checkout instance.

##### return_to: `str`<a id="return_to-str"></a>

Text to display on \\\"Return to Store\\\" button on completing checkout.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Checkout`](./peach_payments_python_sdk/type/checkout.py)
#### 🔄 Return<a id="🔄-return"></a>

[`MessageResponse`](./peach_payments_python_sdk/pydantic/message_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/checkout/validate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peachpayments.files.download_file`<a id="peachpaymentsfilesdownload_file"></a>

Downloads a file that was attached to a payment link.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
peachpayments.files.download_file(
    payment_id="b95d6888-591b-4538-b508-6102cf1259c9",
    file_id="ca6cd55b-4be6-451d-bd72-fe5b7ec1f75z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payment_id: `str`<a id="payment_id-str"></a>

Payment ID.

##### file_id: `str`<a id="file_id-str"></a>

File ID.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/payments/{paymentId}/files/{fileId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peachpayments.files.upload_file`<a id="peachpaymentsfilesupload_file"></a>

Upload a file so that it can be attached to a payment link. Only PDFs smaller than 5 MB are supported.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
upload_file_response = peachpayments.files.upload_file(
    file=open("/path/to/file", "rb"),
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file: `IO`<a id="file-io"></a>

File content to be uploaded.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FilesUploadFileRequest`](./peach_payments_python_sdk/type/files_upload_file_request.py)
File content.

#### 🔄 Return<a id="🔄-return"></a>

[`FilesUploadFileResponse`](./peach_payments_python_sdk/pydantic/files_upload_file_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/attachments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peachpayments.helpers.get_payment_methods`<a id="peachpaymentshelpersget_payment_methods"></a>

Retrieve a list of enabled payment methods for a channel given a particular currency.

For more information, see the [documentation](https://developer.peachpayments.com/docs/checkout-merchant-specs). 


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
peachpayments.helpers.get_payment_methods(
    authentication_entity_id="8ac7a4ca68c22c4d0168c2caab2e0025",
    signature="a668342244a9c77b08a2f9090d033d6e2610b431a5c0ca975f32035ed06164f4",
    currency="ZAR",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authentication_entity_id: `str`<a id="authentication_entity_id-str"></a>

##### signature: `str`<a id="signature-str"></a>

Token to verify the integrity of the request, ensuring that only the merchant sending the request is accepted.

##### currency: `str`<a id="currency-str"></a>

Three-letter ISO 4217 currency code.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`HelpersGetPaymentMethodsRequest`](./peach_payments_python_sdk/type/helpers_get_payment_methods_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/merchant_specs` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peachpayments.payment.cancel_link`<a id="peachpaymentspaymentcancel_link"></a>

Cancel a previously-generated link by supplying the unique paymentId which is returned to you in the payment response.

For more information, see the [documentation](https://developer.peachpayments.com/docs/cancel-link).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
cancel_link_response = peachpayments.payment.cancel_link(
    payment_id="b95d6888-591b-4538-b508-6102cf1259c9",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payment_id: `str`<a id="payment_id-str"></a>

The ID of the payment. Returned when creating a new payment.

#### 🔄 Return<a id="🔄-return"></a>

[`MessageResponse`](./peach_payments_python_sdk/pydantic/message_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/payments/{paymentId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peachpayments.payment.generate_link`<a id="peachpaymentspaymentgenerate_link"></a>

Generate a unique payment link for a transaction and optionally send this link to the recipient via email, SMS, WhatsApp, or a combination of the three.

For more information, see the [documentation](https://developer.peachpayments.com/docs/generate-link-1).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
generate_link_response = peachpayments.payment.generate_link(
    payment={
        "merchant_invoice_id": "INV-9001",
        "amount": 10,
        "currency": "ZAR",
        "notes": "Please pay this at your earliest convenience.",
    },
    customer={
        "given_name": "Jane",
        "surname": "Doe",
        "email": "name@example.com",
        "mobile": "27610107822",
        "whatsapp": "+27123456789",
        "fax": "2919392022",
        "phone": "27210030000",
        "ip": "0.0.0.0",
        "merchant_customer_language": "EN",
        "status": "NEW",
        "merchant_customer_id": "sxxopjqy",
        "tax_id": "4550045030303",
        "tax_type": "tax type",
        "birth_date": "1996-08-07",
    },
    options={
        "send_email": False,
        "send_sms": False,
        "send_whatsapp": False,
        "email_cc": "ccexample@mail.com",
        "email_bcc": "bccexample@mail.com",
        "expiry_time": 5,
        "notification_url": "https://webhook.site/",
    },
    checkout={
        "default_payment_method": "CARD",
        "force_default_method": False,
        "tokenise_card": False,
    },
    entity_id="8ac7a4ca694cec2601694cf5f9360026",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payment: [`GenerateLinkPaymentPayment`](./peach_payments_python_sdk/type/generate_link_payment_payment.py)<a id="payment-generatelinkpaymentpaymentpeach_payments_python_sdktypegenerate_link_payment_paymentpy"></a>


##### customer: [`Customer`](./peach_payments_python_sdk/type/customer.py)<a id="customer-customerpeach_payments_python_sdktypecustomerpy"></a>


##### options: [`PaymentOptions`](./peach_payments_python_sdk/type/payment_options.py)<a id="options-paymentoptionspeach_payments_python_sdktypepayment_optionspy"></a>


##### checkout: [`CheckoutOptions`](./peach_payments_python_sdk/type/checkout_options.py)<a id="checkout-checkoutoptionspeach_payments_python_sdktypecheckout_optionspy"></a>


##### entity_id: `str`<a id="entity_id-str"></a>

The entity for the request.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`GenerateLinkPayment`](./peach_payments_python_sdk/type/generate_link_payment.py)
#### 🔄 Return<a id="🔄-return"></a>

[`GenerateLinkResponse`](./peach_payments_python_sdk/pydantic/generate_link_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/channels/{entityId}/payments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peachpayments.payment.get_all_payment_links`<a id="peachpaymentspaymentget_all_payment_links"></a>

Retrieve a paginated list or export a CSV of all payment links. To export to CSV, change the request header's `Accept` value to `text/csv`. For more information, see the [documentation](https://developer.peachpayments.com/docs/retrieve-all-payment-links), or to try it out, see our [Postman collection](https://www.postman.com/peachpayments/workspace/peach-payments-public-workspace/request/13324425-265d80b0-5baa-478b-be10-debc942ca8f3).

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_payment_links_response = peachpayments.payment.get_all_payment_links(
    merchant="9f6ea39b121d11e89d9774d4352a31dz",
    offset=0,
    per_page=50,
    filters_start_date="2018-03-20T09:12:28Z",
    filters_end_date="2018-03-20T09:12:28Z",
    filters_status="initiated",
    filters_amount_value=100,
    filters_amount_operator="lt",
    filters_sending_options="sendEmail",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### merchant: `str`<a id="merchant-str"></a>

The unique merchant ID to scope the list to. Required if you're exporting payment links to CSV.

##### offset: `int`<a id="offset-int"></a>

The offset from which to read data.

##### per_page: `int`<a id="per_page-int"></a>

The amount of items to retrieve.

##### filters_start_date: `datetime`<a id="filters_start_date-datetime"></a>

Retrieve all payment links from the start date onwards.

##### filters_end_date: `datetime`<a id="filters_end_date-datetime"></a>

Retrieve all payment links until the end date.

##### filters_status: `str`<a id="filters_status-str"></a>

The payment link status to filter on.

##### filters_amount_value: `Union[int, float]`<a id="filters_amount_value-unionint-float"></a>

The amount to filter by.

##### filters_amount_operator: `str`<a id="filters_amount_operator-str"></a>

How to use the amountValue for filtering.

##### filters_sending_options: `str`<a id="filters_sending_options-str"></a>

The sending option to filter on.

#### 🔄 Return<a id="🔄-return"></a>

[`PaymentGetAllPaymentLinksResponse`](./peach_payments_python_sdk/pydantic/payment_get_all_payment_links_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/payments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peachpayments.payments_api_inbound.initiate_debit_transaction`<a id="peachpaymentspayments_api_inboundinitiate_debit_transaction"></a>

Initiate a debit transaction.

Certain parameters are mandatory for specific payment methods and certain parameters act differently depending on the payment method. 

- For 1Voucher, `customer.mobile` (the customer's phone number for receiving change vouchers and refunds) and `virtualAccount.password` (the voucher PIN) are mandatory.
- For M-PESA, `virtualAccount.accountId` (the customer's 12-digit phone number) is mandatory. M-PESA only accepts integer amounts, not decimals, so round up your amount.
- For blink by Emtel and MCB Juice, `virtualAccount.accountId` (the customer's 8-digit phone number) is mandatory.
- For Mobicred, `virtualAccount.accountId` (the customer's Mobicred email address) and `virtualAccount.password` (the customer's Mobicred password) are mandatory.
- For Capitec Pay, `virtualAccount.type` (the customer's identifier type; `IDNUMBER`, `CELLPHONE`, or `ACCOUNTNUMBER`) and `virtualAccount.accountId` (the customer's 13-digit ID number, 10-digit phone number starting with `0`, or up-to 64-digit, alphanumeric bank account number) are mandatory. High-risk merchants must provide the verified `IDNUMBER` and cannot use the `CELLPHONE` or `ACCOUNTNUMBER` account types.
- For EFTsecure, Payflex, ZeroPay, FinChoicePay, Scan to Pay, M-PESA, blink by Emtel, Mobicred, Capitec Pay, Nebank Direct EFT, and MCB Juice, the `shopperResultUrl` is mandatory.

For more information, see the [documentation](https://developer.peachpayments.com/docs/payments-api-flows#payment-flow) and for sample calls, see our [public Postman collection](https://www.postman.com/peachpayments/workspace/peach-payments-public-workspace/request/13324425-693c4b18-dad5-4b6f-aeb0-99bc28b94812).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
initiate_debit_transaction_response = peachpayments.payments_api_inbound.initiate_debit_transaction(
    authentication={
        "user_id": "80d41ee71ee011e98e81067b75644abf",
        "password": "xDZWEIefSkyibutsU3",
        "entity_id": "80d41ee71ee011e98e81067b75644abf",
    },
    merchant_transaction_id="test12345",
    amount="22.50",
    currency="ZAR",
    payment_brand="EFTSECURE",
    payment_type="DB",
    virtual_account={
        "account_id": "80d41ee71ee011e98e81067b75644abf",
        "password": "xDZWEIefSkyibutsU3",
        "token": "fd81f6ccabec11eba6e102d14de18c00",
        "type": "CELLPHONE",
    },
    shipping={
        "street1": "Langtree Lane",
        "city": "Cape Town",
        "state": "Nasarawa",
        "postal_code": "7000",
        "country": "ZA",
        "company": "Business Mosaics Ltd",
        "house_number1": "25567",
        "postcode": "8001",
        "street2": "Loe Street",
    },
    billing={
        "street1": "Langtree Lane",
        "city": "Cape Town",
        "state": "Nasarawa",
        "postal_code": "7000",
        "country": "ZA",
        "company": "Business Mosaics Ltd",
        "house_number1": "25567",
        "postcode": "8001",
        "street2": "Loe Street",
    },
    shopify={
        "order_id": "1234567891234",
        "account_id": "6370",
        "signature": "7292b834263177afa7fddbea3fa7a81f20818ee7cf05d1c4b4cac1677dc7a8f7",
        "test_mode": "false",
    },
    customer={
        "given_name": "Jane",
        "surname": "Doe",
        "email": "name@example.com",
        "mobile": "27610107822",
        "whatsapp": "+27123456789",
        "fax": "2919392022",
        "phone": "27210030000",
        "ip": "0.0.0.0",
        "merchant_customer_language": "EN",
        "status": "NEW",
        "merchant_customer_id": "sxxopjqy",
        "tax_id": "4550045030303",
        "tax_type": "tax type",
        "birth_date": "1996-08-07",
    },
    cart={
        "tax": "15.00",
        "shipping_amount": "22.50",
        "discount": "02.25",
    },
    merchant_invoice_id="20170630407200",
    shopper_result_url="https://example.com/redirect",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authentication: [`Authentication`](./peach_payments_python_sdk/type/authentication.py)<a id="authentication-authenticationpeach_payments_python_sdktypeauthenticationpy"></a>


##### merchant_transaction_id: [`MerchantTransactionId`](./peach_payments_python_sdk/type/merchant_transaction_id.py)<a id="merchant_transaction_id-merchanttransactionidpeach_payments_python_sdktypemerchant_transaction_idpy"></a>

##### amount: [`Amount`](./peach_payments_python_sdk/type/amount.py)<a id="amount-amountpeach_payments_python_sdktypeamountpy"></a>

##### currency: [`Currency`](./peach_payments_python_sdk/type/currency.py)<a id="currency-currencypeach_payments_python_sdktypecurrencypy"></a>

##### payment_brand: [`PaymentBrand`](./peach_payments_python_sdk/type/payment_brand.py)<a id="payment_brand-paymentbrandpeach_payments_python_sdktypepayment_brandpy"></a>

##### payment_type: [`PaymentType`](./peach_payments_python_sdk/type/payment_type.py)<a id="payment_type-paymenttypepeach_payments_python_sdktypepayment_typepy"></a>

##### virtual_account: [`VirtualAccount`](./peach_payments_python_sdk/type/virtual_account.py)<a id="virtual_account-virtualaccountpeach_payments_python_sdktypevirtual_accountpy"></a>


##### shipping: [`Address`](./peach_payments_python_sdk/type/address.py)<a id="shipping-addresspeach_payments_python_sdktypeaddresspy"></a>


##### billing: [`Address`](./peach_payments_python_sdk/type/address.py)<a id="billing-addresspeach_payments_python_sdktypeaddresspy"></a>


##### shopify: [`Shopify`](./peach_payments_python_sdk/type/shopify.py)<a id="shopify-shopifypeach_payments_python_sdktypeshopifypy"></a>


##### customer: [`Customer`](./peach_payments_python_sdk/type/customer.py)<a id="customer-customerpeach_payments_python_sdktypecustomerpy"></a>


##### cart: [`Cart`](./peach_payments_python_sdk/type/cart.py)<a id="cart-cartpeach_payments_python_sdktypecartpy"></a>


##### merchant_invoice_id: [`MerchantInvoiceId`](./peach_payments_python_sdk/type/merchant_invoice_id.py)<a id="merchant_invoice_id-merchantinvoiceidpeach_payments_python_sdktypemerchant_invoice_idpy"></a>

##### shopper_result_url: `str`<a id="shopper_result_url-str"></a>

The Payments API redirects the user to this URL after processing the payment request.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PaymentRequest`](./peach_payments_python_sdk/type/payment_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PaymentsApiInboundInitiateDebitTransactionResponse`](./peach_payments_python_sdk/pydantic/payments_api_inbound_initiate_debit_transaction_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peachpayments.payments_api_inbound.query_transaction_by_id`<a id="peachpaymentspayments_api_inboundquery_transaction_by_id"></a>

Query the status of a transaction using the Peach Payments unique ID.

For more information, see the [documentation](https://developer.peachpayments.com/docs/payments-api-flows#transaction-status-flow).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
query_transaction_by_id_response = (
    peachpayments.payments_api_inbound.query_transaction_by_id(
        unique_id="b4508276b8d146728dac871d6f68b45d",
        authentication_entity_id="80d41ee71ee011e98e81067b75644abf",
        authentication_user_id="80d41ee71ee011e98e81067b75644abf",
        authentication_password="xDZWEIefSkyibutsU3",
    )
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### unique_id: [`UniqueId`](./peach_payments_python_sdk/type/.py)<a id="unique_id-uniqueidpeach_payments_python_sdktypepy"></a>

The Peach Payments unique ID for the transaction.

##### authentication_entity_id: [`EntityId`](./peach_payments_python_sdk/type/.py)<a id="authentication_entity_id-entityidpeach_payments_python_sdktypepy"></a>

Authentication entityId.

##### authentication_user_id: [`UserId`](./peach_payments_python_sdk/type/.py)<a id="authentication_user_id-useridpeach_payments_python_sdktypepy"></a>

Authentication userId.

##### authentication_password: `str`<a id="authentication_password-str"></a>

Authentication password.

#### 🔄 Return<a id="🔄-return"></a>

[`TransactionIdStatusResponse`](./peach_payments_python_sdk/pydantic/transaction_id_status_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payments/{uniqueId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peachpayments.payments_api_inbound.refund_transaction`<a id="peachpaymentspayments_api_inboundrefund_transaction"></a>

Refund a successful debit transaction. You can only refund [certain payment methods](https://developer.peachpayments.com/docs/pp-payment-methods).

For more information, see the [documentation](https://developer.peachpayments.com/docs/payments-api-flows#refund-flow).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
refund_transaction_response = peachpayments.payments_api_inbound.refund_transaction(
    authentication={
        "user_id": "80d41ee71ee011e98e81067b75644abf",
        "password": "xDZWEIefSkyibutsU3",
        "entity_id": "80d41ee71ee011e98e81067b75644abf",
    },
    amount="22.50",
    currency="ZAR",
    payment_type="RF",
    unique_id="b4508276b8d146728dac871d6f68b45d",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authentication: [`Authentication`](./peach_payments_python_sdk/type/authentication.py)<a id="authentication-authenticationpeach_payments_python_sdktypeauthenticationpy"></a>


##### amount: [`Amount`](./peach_payments_python_sdk/type/amount.py)<a id="amount-amountpeach_payments_python_sdktypeamountpy"></a>

##### currency: [`Currency`](./peach_payments_python_sdk/type/currency.py)<a id="currency-currencypeach_payments_python_sdktypecurrencypy"></a>

##### payment_type: [`RefundPaymentType`](./peach_payments_python_sdk/type/refund_payment_type.py)<a id="payment_type-refundpaymenttypepeach_payments_python_sdktyperefund_payment_typepy"></a>

##### unique_id: [`UniqueId`](./peach_payments_python_sdk/type/.py)<a id="unique_id-uniqueidpeach_payments_python_sdktypepy"></a>

The Peach Payments unique ID of the original debit transaction.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`RefundRequest`](./peach_payments_python_sdk/type/refund_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PaymentsApiInboundRefundTransactionResponse`](./peach_payments_python_sdk/pydantic/payments_api_inbound_refund_transaction_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payments/{uniqueId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peachpayments.payments_api_inbound.status`<a id="peachpaymentspayments_api_inboundstatus"></a>

Query the status of a transaction using the merchantTransactionId. Could return multiple results.

For more information, see the [documentation](https://developer.peachpayments.com/docs/payments-api-flows#transaction-status-flow).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
status_response = peachpayments.payments_api_inbound.status(
    authentication_user_id="80d41ee71ee011e98e81067b75644abf",
    authentication_password="xDZWEIefSkyibutsU3",
    authentication_entity_id="80d41ee71ee011e98e81067b75644abf",
    merchant_transaction_id="test12345",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authentication_user_id: [`UserId`](./peach_payments_python_sdk/type/.py)<a id="authentication_user_id-useridpeach_payments_python_sdktypepy"></a>

##### authentication_password: `str`<a id="authentication_password-str"></a>

##### authentication_entity_id: [`EntityId`](./peach_payments_python_sdk/type/.py)<a id="authentication_entity_id-entityidpeach_payments_python_sdktypepy"></a>

##### merchant_transaction_id: [`MerchantTransactionId`](./peach_payments_python_sdk/type/.py)<a id="merchant_transaction_id-merchanttransactionidpeach_payments_python_sdktypepy"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MerchantTransactionIdStatusResponse`](./peach_payments_python_sdk/pydantic/merchant_transaction_id_status_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/payments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peachpayments.payments_api_outbound.webhook`<a id="peachpaymentspayments_api_outboundwebhook"></a>

Encrypted and decrypted webhook sent to merchant - retries if response HTTP status code is not 200.

For more information, see the [documentation](https://developer.peachpayments.com/docs/payments-api-flows#webhook-flow).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
peachpayments.payments_api_outbound.webhook(
    encrypted_data="48d33e173781de4ebfe247593240fee492aad55bc140bd1157b62da5747d74bf349d1c5035ab40bb62ba7ee3eafa7e8f8cf5e3af2cdea0c915eed159d0efa12ccd3c6a4ded4182e26687180a73f1d1ed7ab6415be9f0100a3803d19f1cf90402211185c4fc764be11a1b8d7c5434150db5d74c70e309a701d670c3beef47ea53726c5b7d677e13a0ca4b05a1b4fd7ca4218a3922b45271904f17a8a5c4cbe2b4571928a089610ccf37d14c98ccc51085f0897d22cead18f13504fa2b9182389ed77323ed2c8cacb18f0b1fd8cf0599bfabaac27e0d926d60af3f41f47bf0607c6df031de8973da17fac8ca6eb04c2b6491fa5e73e29cd4f9c3c4fce1c397b729ed6132c7a5fc812dc4bb7173354e7f13f9e80407c9b3c6e5dc82edabbf160097b82438874eb79edd7540ed963c5eb268a74cbbefce1661b388c0e442b4a90a954932e19f49aef5c10c9ac2639085049a2fe3c903aaafed326a2b81e2dcd4e32ac16c72218067c623cd5d20f98ee2594c8557a704c1e7b2a7ac2c7bf8ce52d91e0816081dd88697b0c9ea1b07adaf9a39948f88d02aec37103e52675a394d324db7cab951284f08da17306a1b4107a2b6b5aeead6bdb087fbe927eaf03d9b8e0a4a9683a0966e8d1d8e8ea1069e3870275317d3bc676a697fe4d4b6c0bbabc806ae6ff0d7cec926bfce10eca2f07ac832d6a9984d19b121d99f2db4b33ed6b8ecbf25687c34d8e48ffc1f438a4524c3f9657140102cc55ec0c48d37cb42424e8e622da6fc3f60bd969791b21b6360e25a2bcf956f2cdc1bbf049f173ac0b0558c34f89964cb8aced7bf2b532910d98f83760d529a2e67af7f9a7cd2739b871e7f914a99061623990a64a854560a860c1b5eff565b2de2be64d68be5de3d3a061aabb3ead5039d49d976ea9b094752d1a55851d33be6c1eab4197f1f409150eae8e6fca14ad757bf9c7451a795ab04763b8f1c1d4b3416e055f074aa51c6c5477eb0c219dd9b4bb26926e6490061284e14fa8c6969aba4a8036d685be81de9ad8c834217e456ed0be40e0b2331db8f0240135ac4ae066fe7596c28e949f20af760e6d0836e7ab218ca1092c4d45b64856f286f69d8754622a5a45c1865454c78f6df271481b692f2b5481d09c1d2eba226f40ec1ce008186d286aab4d4e091623e78147b1cbbd4a2c671beca4402565b0d663fc11776085bb5288396cb770bf43281ca14212abc057206684e40181d3e0498eda17e9c5dce344b16dc2853fc6cb3d6e5e86891c8573fb537701a01431cb5d1fe74ef565de48286db8bf17912dc6a46e7413115091d1cb7535e0d08685d57f5a18990cabdd5c73cd193147703f2221c0c2adf1e0bb1d4a170bc38b7082490464cbffcab72ffad243401645e23df324d072bad90200bab1ae40a272bcbd0bf1ccc9595498f0416ec10eb73b7a9024cc9082693c97d98908bc2b34724865dc08f88fbf09ed984b4987c3abf01a30f1d91919f29eecf5849b337512591c1f110de3ea17e0048ff4521820f33adcbb11c1e70b6c7ae646a7e9d024356cf34a5e2ccdbf30c3825e41bdb000d04bd5bda835eb52fd301dece1b11c45d97d03d5048c1a154c0e84e21b066790261632e487ec3c35d877ba79590bac13ea679772d8b2e4821ae3204c34475a2871039835817d10c8db9f3ec241532099dc8d0b4891b23fb12ad173a7be287afe31f3e6e29266c213430b4a749b92bbcfe8ad7ef4281ca7b71502de99adf574f81c5605c70a76295ce51f1f0ce6e475c98c1dc4dfcb3492494cbda9038e8193d072be09f9cf8103d67f79effe972c710accd94a6c5ee0c3e1bf8facb7fee1499a4cbeb5f444de1f85f998698bacbd2b0a8f6f2010bff95d8e75800ff39ea75f18bd0f3729bd24408e464e44d2fb2e62ec6ef06c349b8f1f83cd43bbad21657bece4fb6e115ab12e7a28458b5c8e9ebf5a06dbdd6e459105cab7c69f2792fb21a8b8c05a6498f4b20f42975cedb784ed45898fe3be750af3a23769e5cb7407219044aa4736bffcf66d76459b0c9cb0d7fb91575949beb0b28add0b8f5bb88c63b23643f20954074a561db01dc1fd5fbe0efa0e6e09e0de5fddc84fa12fadf236b9160f7b9a3408919af1e27d81a80f87a65f7038a703f8526d7f85c916223306ee2ba38bba1d3ff01a3c97806ed78fabd5ec298a2716292b852e7d3f7e6575b77457e44b6d22f57f0ae756c2c1c71de0d5278bac29334467949b7fddf6cb4e7d3c5b5b841335a80f9e3c8ed86fe4d0e77d4804418273d6f580f781475ec43edbeb378c172",
    x_initialization_vector="34ba8cf802216b4fab4c3f1z",
    x_authentication_tag="50d697553c37c1f9865acc3dc0f8b5az",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### encrypted_data: `str`<a id="encrypted_data-str"></a>

Encrypted webhook data ciphertext.

##### x_initialization_vector: `str`<a id="x_initialization_vector-str"></a>

##### x_authentication_tag: `str`<a id="x_authentication_tag-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`JSONMerchantWebhook`](./peach_payments_python_sdk/type/json_merchant_webhook.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peachpayments.status.checkout_status_get`<a id="peachpaymentsstatuscheckout_status_get"></a>

Get the status of a checkout instance.

For more information, see the [documentation](https://developer.peachpayments.com/docs/checkout-payment-status).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
checkout_status_get_response = peachpayments.status.checkout_status_get(
    authentication_entity_id="8ac7a4ca68c22c4d0168c2caab2e0025",
    signature="a668342244a9c77b08a2f9090d033d6e2610b431a5c0ca975f32035ed06164f4",
    checkout_id="948cc8dec52a11eb85290242ac130003",
    merchant_transaction_id="OrderNo453432",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### authentication_entity_id: `str`<a id="authentication_entity_id-str"></a>

Merchant's entity ID.

##### signature: `str`<a id="signature-str"></a>

Signature of data signed with secret key of merchant.

##### checkout_id: `str`<a id="checkout_id-str"></a>

Checkout ID.

##### merchant_transaction_id: `str`<a id="merchant_transaction_id-str"></a>

Merchant transaction ID.

#### 🔄 Return<a id="🔄-return"></a>

[`CheckoutStatus`](./peach_payments_python_sdk/pydantic/checkout_status.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/status` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `peachpayments.status.query_payment_status`<a id="peachpaymentsstatusquery_payment_status"></a>

Query the status of a payment.

For more information, see the [documentation](https://developer.peachpayments.com/docs/query-payment).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
query_payment_status_response = peachpayments.status.query_payment_status(
    payment_id="b95d6888-591b-4538-b508-6102cf1259c9",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payment_id: `str`<a id="payment_id-str"></a>

Payment ID. Returned when creating a new payment.

#### 🔄 Return<a id="🔄-return"></a>

[`StatusQueryPaymentStatusResponse`](./peach_payments_python_sdk/pydantic/status_query_payment_status_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/payments/{paymentId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
