provider "aws" {
    region = "ap-south-1"
    profile = "myprofile"
}

resource "tls_private_key" "keyGenerate" {
    algorithm = "RSA"
}

resource "aws_key_pair" "newKey" {
    key_name = "Hadoopclientkey"
    public_key = tls_private_key.keyGenerate.public_key_openssh
}

resource "local_file" "keySave" {
    content = tls_private_key.keyGenerate.private_key_pem
    filename = "Hadoopclientkey.pem"
}

resource "aws_security_group" "hadoopFirewall" {
    name = "hadoopFirewall"
    description = "Open to all"
    ingress {
        from_port = 0
        to_port = 0
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }
    ingress {
	from_port = 22
	to_port = 22
	protocol = "tcp"
	cidr_blocks = ["0.0.0.0/0"]
    }
    egress {
        from_port = 0
        to_port = 0
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }

    tags = {
        Name = "Hadoop-firewall"
    }
}

resource "aws_instance" "Hadoop_client" {
    ami = "ami-0a9d27a9f4f5c0efc"
    instance_type = "t2.micro"
    key_name = aws_key_pair.newKey.key_name 
    security_groups = [ "${aws_security_group.hadoopFirewall.name}"]
    tags = {
        Name = "Hadoop-client"
    }
    depends_on = [
        aws_key_pair.newKey,
        aws_security_group.hadoopFirewall,
    ]
}

output "ClientPublicIP" {
    value = aws_instance.Hadoop_client.public_ip
}

output "ClientKeyName" {
    value = aws_instance.Hadoop_client.key_name
}
