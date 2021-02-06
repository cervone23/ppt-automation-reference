import streamlit as st

# Python Functions Page -----------------------------------------

def app():
    st.title('Python Functions Code Reference')
    st.write('Sample Python Functions Code')

    st.subheader('Upload File to GC Bucket & Return URL Link')
    code = """

    bucket_name= 'bucket_name'
    blob_name = 'blob name'
    path_to_file = 'file'

    def upload_to_bucket(blob_name, path_to_file, bucket_name):
        # Upload data to a google cloud bucket and get public URL#
        # Explicitly use service account credentials by specifying the private key
        # file.
        storage_client = storage.Client.from_service_account_json(
            'xxxxxx_gcloud.json'
        )
        # print(buckets = list(storage_client.list_buckets())
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_filename(path_to_file)
        # returns a public url
        blob.make_public()
        return blob.public_url """

    st.code(code, language="python")
