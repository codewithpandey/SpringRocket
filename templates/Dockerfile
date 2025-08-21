FROM maven:3.9.1-eclipse-temurin-17
WORKDIR /app
COPY . .
RUN mvn package
CMD ["java", "-jar", "target/{{ServiceName}}.jar"]
