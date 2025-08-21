package com.example.{{ServiceName}};

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/{{service_name_lower}}/billing")
public class BillingController {

    @PostMapping("/subscribe/stripe")
    public String subscribeStripe() {
        // Placeholder: Integrate Stripe subscription here
        return "Stripe subscription endpoint for {{ServiceName}}";
    }

    @PostMapping("/subscribe/paypal")
    public String subscribePayPal() {
        // Placeholder: Integrate PayPal subscription here
        return "PayPal subscription endpoint for {{ServiceName}}";
    }
}
