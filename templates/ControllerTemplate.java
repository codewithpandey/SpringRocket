package com.example.{{ServiceName}};

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/{{service_name_lower}}")
public class Controller {
    @GetMapping
    public String hello() {
        return "Hello from {{ServiceName}}";
    }
}
