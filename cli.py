import click
import os
from jinja2 import Template

TEMPLATES_DIR = "templates"
SERVICES_DIR = "services"

def render_template(template_path, dest_path, context):
    with open(template_path) as f:
        template = Template(f.read())
        rendered = template.render(context)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(rendered)

@click.group()
def cli():
    pass

@cli.command()
@click.argument("service_name")
@click.option("--docker", is_flag=True, help="Include Dockerfile")
@click.option("--db", is_flag=True, help="Include DB config")
@click.option("--billing", is_flag=True, help="Include sample billing controller")
def create_service(service_name, docker, db, billing):
    """Generate a new microservice boilerplate"""
    context = {
        "ServiceName": service_name,
        "service_name_lower": service_name.lower()
    }

    # Create service directory structure
    if not service_name.isidentifier():
        click.echo(f"Error: '{service_name}' is not a valid service name. Use a valid identifier.")
        return
    #Create Service Root Directory
    service_path = os.path.join(SERVICES_DIR, service_name)
    os.makedirs(service_path, exist_ok=True)

    # Create service directory
    project_path = os.path.join(SERVICES_DIR, service_name, "src/main/java/com/example")
    os.makedirs(project_path, exist_ok=True)

    # Create resources directory
    resources_path = os.path.join(SERVICES_DIR, service_name, "src/main/resources")
    os.makedirs(resources_path, exist_ok=True)

    # Create test directory
    test_path = os.path.join(SERVICES_DIR, service_name, "src/test/java/com/example")
    os.makedirs(test_path, exist_ok=True)

    # Create test resources directory
    test_resources_path = os.path.join(SERVICES_DIR, service_name, "src/test/resources")
    os.makedirs(test_resources_path, exist_ok=True) 
    
    # Java files
    render_template(f"{TEMPLATES_DIR}/ApplicationTemplate.java",
                    f"{project_path}/Application.java", context)
    render_template(f"{TEMPLATES_DIR}/ControllerTemplate.java",
                    f"{project_path}/Controller.java", context)

    # Optional BillingController
    if billing:
        render_template(f"{TEMPLATES_DIR}/BillingControllerTemplate.java",
                        f"{project_path}/BillingController.java", context)
                        
        # Testfiles for BillingController
        render_template(f"{TEMPLATES_DIR}/BillingControllerTestTemplate.java",
                        f"{test_path}/BillingControllerTest.java", context)
    # Test files
    render_template(f"{TEMPLATES_DIR}/ApplicationTestTemplate.java",
                    f"{test_path}/ApplicationTest.java", context)
    render_template(f"{TEMPLATES_DIR}/ControllerTestTemplate.java",
                    f"{test_path}/ControllerTest.java", context)    

    # pom.xml
    render_template(f"{TEMPLATES_DIR}/pom.xml",
                    f"{service_path}/pom.xml", context)

    # DB config
    if db:
        render_template(f"{TEMPLATES_DIR}/application.properties",
                        f"{resources_path}/application.properties", context)
        # application-test.properties
        render_template(f"{TEMPLATES_DIR}/application-test.properties",
                        f"{test_resources_path}/application-test.properties", context)
        

    # Dockerfile
    if docker:
        render_template(f"{TEMPLATES_DIR}/Dockerfile",
                        f"{service_path}/Dockerfile", context)

    # README.md
    render_template(f"{TEMPLATES_DIR}/READMETemplate.md",
                    f"{service_path}/README.md", context)

    click.echo(f"Service '{service_name}' generated in {service_path}")

if __name__ == "__main__":
    cli()
