=begin
#MetaDefender Core

### Developer Guide This is the API documentation for *MetaDefender Core Public API*.  If you would like to evaluate or have any questions about this documentation, please contact us via our [Contact Us](https://opswat.com/contact) form.  ## How to Interact with MetaDefender Core using REST Beginning with MetaDefender Core 4.x, OPSWAT recommends using the JSON-based REST API. The available methods are documented below. > _**Note**:_ MetaDefender API doesn't support chunk upload, however is recommended to stream the files to MetaDefender as part of the upload process.  --- ## File Analysis Process    MetaDefender's main functionality is to analyze large volumes with a high throughput. Depending on the configuration and licensed technologies, the analysis times can vary.    Below is a brief description of the API integration flow:    1. Upload a file for analysis (`POST /file`), which returns the `data_id`: [File Analysis](#operation/fileAnalysisPost)).           > _**Note**:_ The performance depends on:           > - number of nodes (scaling)     > - number of engines per node     > - type of file to be scanned     > - Metadefender Core and nodes' hardware       2. You have 2 ways to retrieve the analysis report:      - **Polling**: Fetch the result with previously received data_id (`GET /file/{data_id}` resource) until scan result belonging to data_id doesn't reach the 100 percent progress_percentage: ( [Fetch processing result](#operation/userLogin))        > _**Note**:_ Too many data_id requests can reduce performance. It is enough to just check every few hundred milliseconds.          - **Callbackurl**: Specify a callbackurl that will be called once the analysis is complete.     3. Retrieve the analysis results anytime after the analysis is completed with hash for files (md5, sha1, sha256) by calling [Fetch processing result](#operation/userLogin).      - The hash can be found in the scan results    4. Retrieve processed file (sanitized, redacted, watermarked, etc.) after the analysis is complete.      > _**Note**:_ Based on the configured retention policy, the files might be available for retrieval at a later time.   --- OPSWAT provides some sample codes on [GitHub](https://github.com/OPSWAT) to make it easier to understand how the MetaDefender REST API works. 

The version of the OpenAPI document: v4.18.0
Contact: feedback@opswat.com
Generated by: https://openapi-generator.tech
OpenAPI Generator version: 4.3.0

=end

require 'spec_helper'
require 'json'

# Unit tests for OpenapiClient::BatchApi
# Automatically generated by openapi-generator (https://openapi-generator.tech)
# Please update as you see appropriate
describe 'BatchApi' do
  before do
    # run before each test
    @api_instance = OpenapiClient::BatchApi.new
  end

  after do
    # run after each test
  end

  describe 'test an instance of BatchApi' do
    it 'should create an instance of BatchApi' do
      expect(@api_instance).to be_instance_of(OpenapiClient::BatchApi)
    end
  end

  # unit tests for batch_cancel
  # Cancel Batch
  # When cancelling a batch, the connected analysis that are still in progress will be cancelled also.   The cancelled batch will be closed.      
  # @param batch_id The batch identifier used to submit files in the batch and to close the batch.
  # @param [Hash] opts the optional parameters
  # @option opts [String] :apikey Generated &#x60;session_id&#x60; from [Login](#operation/userLogin) call can be used as an &#x60;apikey&#x60; for API calls that require authentication.                
  # @return [Object]
  describe 'batch_cancel test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for batch_close
  # Close Batch
  # The batch will be closed and files can no longer can be added to the current batch.      
  # @param batch_id The batch identifier used to submit files in the batch and to close the batch.
  # @param [Hash] opts the optional parameters
  # @option opts [String] :apikey Generated &#x60;session_id&#x60; from [Login](#operation/userLogin) call can be used as an &#x60;apikey&#x60; for API calls that require authentication.                
  # @return [BatchResponse]
  describe 'batch_close test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for batch_create
  # Initiate Batch
  # Create a new batch and retrieve the batch_id
  # @param [Hash] opts the optional parameters
  # @option opts [String] :apikey Generated &#x60;session_id&#x60; from [Login](#operation/userLogin) call can be used as an &#x60;apikey&#x60; for API calls that require authentication.                
  # @option opts [String] :rule Select rule for the analysis, if no header given the default rule will be selected (URL encoded string of rule name)       
  # @option opts [String] :user_agent user_agent header used to identify (and limit) access to a particular rule. For rule selection, &#x60;rule&#x60; header should be used. 
  # @option opts [String] :user_data Additional custom information (max 1024 bytes, URL encoded UTF-8 string)       
  # @return [BatchId]
  describe 'batch_create test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for batch_signed_result
  # Download Signed Batch Result
  # Download digitally signed status report for the entire batch
  # @param batch_id The batch identifier used to submit files in the batch and to close the batch.
  # @param [Hash] opts the optional parameters
  # @option opts [String] :apikey Generated &#x60;session_id&#x60; from [Login](#operation/userLogin) call can be used as an &#x60;apikey&#x60; for API calls that require authentication.                
  # @return [nil]
  describe 'batch_signed_result test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

  # unit tests for batch_status
  # Status of Batch Analysis
  # Retrieve status report for the entire batch
  # @param batch_id The batch identifier used to submit files in the batch and to close the batch.
  # @param [Hash] opts the optional parameters
  # @option opts [String] :apikey Generated &#x60;session_id&#x60; from [Login](#operation/userLogin) call can be used as an &#x60;apikey&#x60; for API calls that require authentication.                
  # @return [BatchResponse]
  describe 'batch_status test' do
    it 'should work' do
      # assertion here. ref: https://www.relishapp.com/rspec/rspec-expectations/docs/built-in-matchers
    end
  end

end