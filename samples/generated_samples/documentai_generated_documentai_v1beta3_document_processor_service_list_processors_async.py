# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated code. DO NOT EDIT!
#
# Snippet for ListProcessors
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-documentai


# [START documentai_generated_documentai_v1beta3_DocumentProcessorService_ListProcessors_async]
from google.cloud import documentai_v1beta3


async def sample_list_processors():
    # Create a client
    client = documentai_v1beta3.DocumentProcessorServiceAsyncClient()

    # Initialize request argument(s)
    project = "my-project-id"
    location = "us-central1"
    processor = "processor_value"
    parent = f"projects/{project}/locations/{location}/processors/{processor}"

    request = documentai_v1beta3.ListProcessorsRequest(
        parent=parent,
    )

    # Make the request
    page_result = client.list_processors(request=request)
    async for response in page_result:
        print(response)

# [END documentai_generated_documentai_v1beta3_DocumentProcessorService_ListProcessors_async]
