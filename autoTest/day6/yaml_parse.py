
import yaml
f=open(file="swagger.yaml")
swagger=yaml.load(f,yaml.FullLoader)
print(swagger)
print(swagger['info'])