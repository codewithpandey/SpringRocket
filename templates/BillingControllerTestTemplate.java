package com.example;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.test.web.servlet.MockMvc;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

@WebMvcTest(BillingController.class)
class BillingControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @Test
    void testStripeSubscribe() throws Exception {
        mockMvc.perform(post("/api/billing/subscribe/stripe"))
               .andExpect(status().isOk())
               .andExpect(content().string("Stripe subscription placeholder"));
    }

    @Test
    void testPaypalSubscribe() throws Exception {
        mockMvc.perform(post("/api/billing/subscribe/paypal"))
               .andExpect(status().isOk())
               .andExpect(content().string("PayPal subscription placeholder"));
    }
}
