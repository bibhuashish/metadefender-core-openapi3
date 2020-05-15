=begin
#MetaDefender Core

### Developer Guide This is the API documentation for *MetaDefender Core Public API*.  If you would like to evaluate or have any questions about this documentation, please contact us via our [Contact Us](https://opswat.com/contact) form.  ## How to Interact with MetaDefender Core using REST Beginning with MetaDefender Core 4.x, OPSWAT recommends using the JSON-based REST API. The available methods are documented below. > _**Note**:_ MetaDefender API doesn't support chunk upload, however is recommended to stream the files to MetaDefender as part of the upload process.  --- ## File Analysis Process    MetaDefender's main functionality is to analyze large volumes with a high throughput. Depending on the configuration and licensed technologies, the analysis times can vary.    Below is a brief description of the API integration flow:    1. Upload a file for analysis (`POST /file`), which returns the `data_id`: [File Analysis](#operation/fileAnalysisPost)).           > _**Note**:_ The performance depends on:           > - number of nodes (scaling)     > - number of engines per node     > - type of file to be scanned     > - Metadefender Core and nodes' hardware       2. You have 2 ways to retrieve the analysis report:      - **Polling**: Fetch the result with previously received data_id (`GET /file/{data_id}` resource) until scan result belonging to data_id doesn't reach the 100 percent progress_percentage: ( [Fetch processing result](#operation/userLogin))        > _**Note**:_ Too many data_id requests can reduce performance. It is enough to just check every few hundred milliseconds.          - **Callbackurl**: Specify a callbackurl that will be called once the analysis is complete.     3. Retrieve the analysis results anytime after the analysis is completed with hash for files (md5, sha1, sha256) by calling [Fetch processing result](#operation/userLogin).      - The hash can be found in the scan results    4. Retrieve processed file (sanitized, redacted, watermarked, etc.) after the analysis is complete.      > _**Note**:_ Based on the configured retention policy, the files might be available for retrieval at a later time.   --- OPSWAT provides some sample codes on [GitHub](https://github.com/OPSWAT) to make it easier to understand how the MetaDefender REST API works. 

The version of the OpenAPI document: v4.18.0
Contact: feedback@opswat.com
Generated by: https://openapi-generator.tech
OpenAPI Generator version: 4.3.0

=end

require 'cgi'

module OpenapiClient
  class AdminApi
    attr_accessor :api_client

    def initialize(api_client = ApiClient.default)
      @api_client = api_client
    end
    # Import configuration
    # Import configuration from file.
    # @param [Hash] opts the optional parameters
    # @option opts [String] :apikey Generated &#x60;session_id&#x60; from [Login](#operation/userLogin) call can be used as an &#x60;apikey&#x60; for API calls that require authentication.                
    # @option opts [File] :body 
    # @return [InlineResponse2006]
    def admin_import(opts = {})
      data, _status_code, _headers = admin_import_with_http_info(opts)
      data
    end

    # Import configuration
    # Import configuration from file.
    # @param [Hash] opts the optional parameters
    # @option opts [String] :apikey Generated &#x60;session_id&#x60; from [Login](#operation/userLogin) call can be used as an &#x60;apikey&#x60; for API calls that require authentication.                
    # @option opts [File] :body 
    # @return [Array<(InlineResponse2006, Integer, Hash)>] InlineResponse2006 data, response status code and response headers
    def admin_import_with_http_info(opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: AdminApi.admin_import ...'
      end
      # resource path
      local_var_path = '/admin/import'

      # query parameters
      query_params = opts[:query_params] || {}

      # header parameters
      header_params = opts[:header_params] || {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json'])
      # HTTP header 'Content-Type'
      header_params['Content-Type'] = @api_client.select_header_content_type(['application/json'])
      header_params[:'apikey'] = opts[:'apikey'] if !opts[:'apikey'].nil?

      # form parameters
      form_params = opts[:form_params] || {}

      # http body (model)
      post_body = opts[:body] || @api_client.object_to_http_body(opts[:'body']) 

      # return_type
      return_type = opts[:return_type] || 'InlineResponse2006' 

      # auth_names
      auth_names = opts[:auth_names] || ['apikey']

      new_options = opts.merge(
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:POST, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: AdminApi#admin_import\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # Create new role
    # Add a new user role to the system.
    # @param [Hash] opts the optional parameters
    # @option opts [String] :apikey Generated &#x60;session_id&#x60; from [Login](#operation/userLogin) call can be used as an &#x60;apikey&#x60; for API calls that require authentication.                
    # @option opts [NewUserRoleRequest] :new_user_role_request 
    # @return [NewUserRoleResponse]
    def role_create(opts = {})
      data, _status_code, _headers = role_create_with_http_info(opts)
      data
    end

    # Create new role
    # Add a new user role to the system.
    # @param [Hash] opts the optional parameters
    # @option opts [String] :apikey Generated &#x60;session_id&#x60; from [Login](#operation/userLogin) call can be used as an &#x60;apikey&#x60; for API calls that require authentication.                
    # @option opts [NewUserRoleRequest] :new_user_role_request 
    # @return [Array<(NewUserRoleResponse, Integer, Hash)>] NewUserRoleResponse data, response status code and response headers
    def role_create_with_http_info(opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: AdminApi.role_create ...'
      end
      # resource path
      local_var_path = '/admin/role'

      # query parameters
      query_params = opts[:query_params] || {}

      # header parameters
      header_params = opts[:header_params] || {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json'])
      # HTTP header 'Content-Type'
      header_params['Content-Type'] = @api_client.select_header_content_type(['application/json'])
      header_params[:'apikey'] = opts[:'apikey'] if !opts[:'apikey'].nil?

      # form parameters
      form_params = opts[:form_params] || {}

      # http body (model)
      post_body = opts[:body] || @api_client.object_to_http_body(opts[:'new_user_role_request']) 

      # return_type
      return_type = opts[:return_type] || 'NewUserRoleResponse' 

      # auth_names
      auth_names = opts[:auth_names] || ['apikey']

      new_options = opts.merge(
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:POST, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: AdminApi#role_create\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end

    # Create user
    # 
    # @param [Hash] opts the optional parameters
    # @option opts [String] :apikey Generated &#x60;session_id&#x60; from [Login](#operation/userLogin) call can be used as an &#x60;apikey&#x60; for API calls that require authentication.                
    # @option opts [UserRequest] :user_request 
    # @return [UserResponse]
    def user_create(opts = {})
      data, _status_code, _headers = user_create_with_http_info(opts)
      data
    end

    # Create user
    # 
    # @param [Hash] opts the optional parameters
    # @option opts [String] :apikey Generated &#x60;session_id&#x60; from [Login](#operation/userLogin) call can be used as an &#x60;apikey&#x60; for API calls that require authentication.                
    # @option opts [UserRequest] :user_request 
    # @return [Array<(UserResponse, Integer, Hash)>] UserResponse data, response status code and response headers
    def user_create_with_http_info(opts = {})
      if @api_client.config.debugging
        @api_client.config.logger.debug 'Calling API: AdminApi.user_create ...'
      end
      # resource path
      local_var_path = '/admin/user'

      # query parameters
      query_params = opts[:query_params] || {}

      # header parameters
      header_params = opts[:header_params] || {}
      # HTTP header 'Accept' (if needed)
      header_params['Accept'] = @api_client.select_header_accept(['application/json'])
      # HTTP header 'Content-Type'
      header_params['Content-Type'] = @api_client.select_header_content_type(['application/json'])
      header_params[:'apikey'] = opts[:'apikey'] if !opts[:'apikey'].nil?

      # form parameters
      form_params = opts[:form_params] || {}

      # http body (model)
      post_body = opts[:body] || @api_client.object_to_http_body(opts[:'user_request']) 

      # return_type
      return_type = opts[:return_type] || 'UserResponse' 

      # auth_names
      auth_names = opts[:auth_names] || ['apikey']

      new_options = opts.merge(
        :header_params => header_params,
        :query_params => query_params,
        :form_params => form_params,
        :body => post_body,
        :auth_names => auth_names,
        :return_type => return_type
      )

      data, status_code, headers = @api_client.call_api(:POST, local_var_path, new_options)
      if @api_client.config.debugging
        @api_client.config.logger.debug "API called: AdminApi#user_create\nData: #{data.inspect}\nStatus code: #{status_code}\nHeaders: #{headers}"
      end
      return data, status_code, headers
    end
  end
end