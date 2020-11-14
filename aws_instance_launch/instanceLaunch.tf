provider "aws" {
    region = "ap-south-1"
    profile = "myprofile"
}

resource "tls_private_key" "keyGenerate" {
    algorithm = "RSA"
}

resource "aws_key_pair" "newKey" {
    key_name = "Hadoopkey"
    public_key = tls_private_key.keyGenerate.public_key_openssh
}

resource "local_file" "keySave" {
    content = tls_private_key.keyGenerate.private_key_pem
    filename = "Hadoopkey.pem"
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

resource "aws_instance" "Hadoop_master" {
    ami = "ami-052c08d70def0ac62"
    instance_type = "t2.micro"
    key_name = aws_key_pair.newKey.key_name 
    security_groups = [ "${aws_security_group.hadoopFirewall.name}"]
    count = 1
    tags = {
        Name = "Hadoop-master"
    }
    depends_on = [
        aws_key_pair.newKey,
        aws_security_group.hadoopFirewall,
    ]
}


