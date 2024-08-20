media_types = {
    '.gif': 'image/gif',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.png': 'image/png',
    '.pdf': 'application/pdf',
    '.txt': 'text/plain',
    '.zip': 'application/zip'
}

file_name = input("Enter the file name: ").strip()

file_name_lower = file_name.lower()

media_type = 'application/octet-stream'

for suffix in media_types:
    if file_name_lower.endswith(suffix):
        media_type = media_types[suffix]
        break

print(media_type)