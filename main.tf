terraform {
  required_providers {
    digitalocean = {
      source = "digitalocean/digitalocean"
      version = "~> 2.0"
    }
  }
}

# Set the variable value in *.tfvars file
# or using -var="do_token=..." CLI option
variable "do_token" {}

# Configure the DigitalOcean Provider
provider "digitalocean" {
  token = var.do_token
}


resource "digitalocean_app" "todo-list-take-1" {
  spec {
    name   = "todo-list-take-1"
    region = "nyc1"

    service {
      name               = "todo-list-service"      
      instance_count     = 1
      instance_size_slug = "professional-xs"
      run_command        = "python manage.py migrate && gunicorn app.wsgi --worker-tmp-dir /dev/shm --workers 3 --threads 3"
      

      github {
        repo           = "thiagoferreiraw/django-todo-list"
        branch         = "cursor-pagination"
        deploy_on_push = true

      }
    }

    env {
      key = "DATABASE_URL"
      value = "postgresql://abc"
      type = "SECRET"
    }

    env {
      key = "REPLICA_URLS"
      value = "postgresql://abc,postgresql://def"
      type = "SECRET"
    }
  }
}
