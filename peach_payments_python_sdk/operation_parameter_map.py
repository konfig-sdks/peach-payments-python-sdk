operation_parameter_map = {
    '/api/channels/{entityId}/payments/batches-POST': {
        'parameters': [
            {
                'name': 'filename'
            },
            {
                'name': 'entityId'
            },
            {
                'name': 'notificationUrl'
            },
        ]
    },
    '/api/channels/{entityId}/payments/batches-GET': {
        'parameters': [
            {
                'name': 'entityId'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'perPage'
            },
            {
                'name': 'filters[startDate]'
            },
            {
                'name': 'filters[endDate]'
            },
            {
                'name': 'filters[status]'
            },
        ]
    },
    '/api/batches/{batchId}/files-GET': {
        'parameters': [
            {
                'name': 'batchId'
            },
        ]
    },
    '/api/batches/{batchId}-GET': {
        'parameters': [
            {
                'name': 'batchId'
            },
        ]
    },
    '/v2/checkout-POST': {
        'parameters': [
            {
                'name': 'authentication.entityId'
            },
            {
                'name': 'merchantTransactionId'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'nonce'
            },
            {
                'name': 'shopperResultUrl'
            },
            {
                'name': 'Referer'
            },
            {
                'name': 'defaultPaymentMethod'
            },
            {
                'name': 'forceDefaultMethod'
            },
            {
                'name': 'merchantInvoiceId'
            },
            {
                'name': 'cancelUrl'
            },
            {
                'name': 'notificationUrl'
            },
            {
                'name': 'customParameters'
            },
            {
                'name': 'customer'
            },
            {
                'name': 'billing'
            },
            {
                'name': 'shipping'
            },
            {
                'name': 'createRegistration'
            },
            {
                'name': 'originator'
            },
            {
                'name': 'returnTo'
            },
        ]
    },
    '/checkout-POST': {
        'parameters': [
            {
                'name': 'Referer'
            },
            {
                'name': 'authentication.entityId'
            },
            {
                'name': 'signature'
            },
            {
                'name': 'merchantTransactionId'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'paymentType'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'nonce'
            },
            {
                'name': 'shopperResultUrl'
            },
            {
                'name': 'defaultPaymentMethod'
            },
            {
                'name': 'forceDefaultMethod'
            },
            {
                'name': 'merchantInvoiceId'
            },
            {
                'name': 'cancelUrl'
            },
            {
                'name': 'notificationUrl'
            },
            {
                'name': 'customParameters[name]'
            },
            {
                'name': 'customer.merchantCustomerId'
            },
            {
                'name': 'customer.givenName'
            },
            {
                'name': 'customer.surname'
            },
            {
                'name': 'customer.mobile'
            },
            {
                'name': 'customer.email'
            },
            {
                'name': 'customer.status'
            },
            {
                'name': 'customer.birthDate'
            },
            {
                'name': 'customer.ip'
            },
            {
                'name': 'customer.phone'
            },
            {
                'name': 'customer.idNumber'
            },
            {
                'name': 'billing.street1'
            },
            {
                'name': 'billing.street2'
            },
            {
                'name': 'billing.city'
            },
            {
                'name': 'billing.company'
            },
            {
                'name': 'billing.country'
            },
            {
                'name': 'billing.state'
            },
            {
                'name': 'billing.postcode'
            },
            {
                'name': 'shipping.street1'
            },
            {
                'name': 'shipping.street2'
            },
            {
                'name': 'shipping.city'
            },
            {
                'name': 'shipping.company'
            },
            {
                'name': 'shipping.postcode'
            },
            {
                'name': 'shipping.country'
            },
            {
                'name': 'shipping.state'
            },
            {
                'name': 'cart.tax'
            },
            {
                'name': 'cart.shippingAmount'
            },
            {
                'name': 'cart.discount'
            },
            {
                'name': 'createRegistration'
            },
            {
                'name': 'originator'
            },
            {
                'name': 'returnTo'
            },
        ]
    },
    '/checkout/initiate-POST': {
        'parameters': [
            {
                'name': 'authentication.entityId'
            },
            {
                'name': 'signature'
            },
            {
                'name': 'merchantTransactionId'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'paymentType'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'nonce'
            },
            {
                'name': 'shopperResultUrl'
            },
            {
                'name': 'Referer'
            },
            {
                'name': 'defaultPaymentMethod'
            },
            {
                'name': 'forceDefaultMethod'
            },
            {
                'name': 'merchantInvoiceId'
            },
            {
                'name': 'cancelUrl'
            },
            {
                'name': 'notificationUrl'
            },
            {
                'name': 'customParameters[name]'
            },
            {
                'name': 'customer.merchantCustomerId'
            },
            {
                'name': 'customer.givenName'
            },
            {
                'name': 'customer.surname'
            },
            {
                'name': 'customer.mobile'
            },
            {
                'name': 'customer.email'
            },
            {
                'name': 'customer.status'
            },
            {
                'name': 'customer.birthDate'
            },
            {
                'name': 'customer.ip'
            },
            {
                'name': 'customer.phone'
            },
            {
                'name': 'customer.idNumber'
            },
            {
                'name': 'billing.street1'
            },
            {
                'name': 'billing.street2'
            },
            {
                'name': 'billing.city'
            },
            {
                'name': 'billing.company'
            },
            {
                'name': 'billing.country'
            },
            {
                'name': 'billing.state'
            },
            {
                'name': 'billing.postcode'
            },
            {
                'name': 'shipping.street1'
            },
            {
                'name': 'shipping.street2'
            },
            {
                'name': 'shipping.city'
            },
            {
                'name': 'shipping.company'
            },
            {
                'name': 'shipping.postcode'
            },
            {
                'name': 'shipping.country'
            },
            {
                'name': 'shipping.state'
            },
            {
                'name': 'cart.tax'
            },
            {
                'name': 'cart.shippingAmount'
            },
            {
                'name': 'cart.discount'
            },
            {
                'name': 'createRegistration'
            },
            {
                'name': 'originator'
            },
            {
                'name': 'returnTo'
            },
        ]
    },
    '/checkout/validate-POST': {
        'parameters': [
            {
                'name': 'authentication.entityId'
            },
            {
                'name': 'signature'
            },
            {
                'name': 'merchantTransactionId'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'paymentType'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'nonce'
            },
            {
                'name': 'shopperResultUrl'
            },
            {
                'name': 'Referer'
            },
            {
                'name': 'defaultPaymentMethod'
            },
            {
                'name': 'forceDefaultMethod'
            },
            {
                'name': 'merchantInvoiceId'
            },
            {
                'name': 'cancelUrl'
            },
            {
                'name': 'notificationUrl'
            },
            {
                'name': 'customParameters[name]'
            },
            {
                'name': 'customer.merchantCustomerId'
            },
            {
                'name': 'customer.givenName'
            },
            {
                'name': 'customer.surname'
            },
            {
                'name': 'customer.mobile'
            },
            {
                'name': 'customer.email'
            },
            {
                'name': 'customer.status'
            },
            {
                'name': 'customer.birthDate'
            },
            {
                'name': 'customer.ip'
            },
            {
                'name': 'customer.phone'
            },
            {
                'name': 'customer.idNumber'
            },
            {
                'name': 'billing.street1'
            },
            {
                'name': 'billing.street2'
            },
            {
                'name': 'billing.city'
            },
            {
                'name': 'billing.company'
            },
            {
                'name': 'billing.country'
            },
            {
                'name': 'billing.state'
            },
            {
                'name': 'billing.postcode'
            },
            {
                'name': 'shipping.street1'
            },
            {
                'name': 'shipping.street2'
            },
            {
                'name': 'shipping.city'
            },
            {
                'name': 'shipping.company'
            },
            {
                'name': 'shipping.postcode'
            },
            {
                'name': 'shipping.country'
            },
            {
                'name': 'shipping.state'
            },
            {
                'name': 'cart.tax'
            },
            {
                'name': 'cart.shippingAmount'
            },
            {
                'name': 'cart.discount'
            },
            {
                'name': 'createRegistration'
            },
            {
                'name': 'originator'
            },
            {
                'name': 'returnTo'
            },
        ]
    },
    '/api/payments/{paymentId}/files/{fileId}-GET': {
        'parameters': [
            {
                'name': 'paymentId'
            },
            {
                'name': 'fileId'
            },
        ]
    },
    '/api/attachments-POST': {
        'parameters': [
            {
                'name': 'file'
            },
        ]
    },
    '/merchant_specs-POST': {
        'parameters': [
            {
                'name': 'authentication.entityId'
            },
            {
                'name': 'signature'
            },
            {
                'name': 'currency'
            },
        ]
    },
    '/api/payments/{paymentId}-DELETE': {
        'parameters': [
            {
                'name': 'paymentId'
            },
        ]
    },
    '/api/channels/{entityId}/payments-POST': {
        'parameters': [
            {
                'name': 'payment'
            },
            {
                'name': 'customer'
            },
            {
                'name': 'options'
            },
            {
                'name': 'checkout'
            },
            {
                'name': 'entityId'
            },
        ]
    },
    '/api/payments-GET': {
        'parameters': [
            {
                'name': 'merchant'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'perPage'
            },
            {
                'name': 'filters[startDate]'
            },
            {
                'name': 'filters[endDate]'
            },
            {
                'name': 'filters[status]'
            },
            {
                'name': 'filters[amountValue]'
            },
            {
                'name': 'filters[amountOperator]'
            },
            {
                'name': 'filters[sendingOptions]'
            },
        ]
    },
    '/payments-POST': {
        'parameters': [
            {
                'name': 'authentication'
            },
            {
                'name': 'merchantTransactionId'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'paymentBrand'
            },
            {
                'name': 'paymentType'
            },
            {
                'name': 'virtualAccount'
            },
            {
                'name': 'shipping'
            },
            {
                'name': 'billing'
            },
            {
                'name': 'shopify'
            },
            {
                'name': 'customer'
            },
            {
                'name': 'cart'
            },
            {
                'name': 'merchantInvoiceId'
            },
            {
                'name': 'shopperResultUrl'
            },
        ]
    },
    '/payments/{uniqueId}-GET': {
        'parameters': [
            {
                'name': 'uniqueId'
            },
            {
                'name': 'authentication.entityId'
            },
            {
                'name': 'authentication.userId'
            },
            {
                'name': 'authentication.password'
            },
        ]
    },
    '/payments/{uniqueId}-POST': {
        'parameters': [
            {
                'name': 'authentication'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'paymentType'
            },
            {
                'name': 'uniqueId'
            },
        ]
    },
    '/payments-GET': {
        'parameters': [
            {
                'name': 'authentication.userId'
            },
            {
                'name': 'authentication.password'
            },
            {
                'name': 'authentication.entityId'
            },
            {
                'name': 'merchantTransactionId'
            },
        ]
    },
    '/-POST': {
        'parameters': [
            {
                'name': 'encryptedData'
            },
            {
                'name': 'X-Initialization-Vector'
            },
            {
                'name': 'X-Authentication-Tag'
            },
        ]
    },
    '/status-GET': {
        'parameters': [
            {
                'name': 'authentication.entityId'
            },
            {
                'name': 'signature'
            },
            {
                'name': 'checkoutId'
            },
            {
                'name': 'merchantTransactionId'
            },
        ]
    },
    '/api/payments/{paymentId}-GET': {
        'parameters': [
            {
                'name': 'paymentId'
            },
        ]
    },
};