=begin comment

MetaDefender Core

## Developer Guide This is the API documentation for *MetaDefender Core Public API*.  If you would like to evaluate or have any questions about this documentation, please contact us via our [Contact Us](https://opswat.com/contact) form.  ## How to Interact with MetaDefender Core using REST Beginning with MetaDefender Core 4.x, OPSWAT recommends using the JSON-based REST API. The available methods are documented below. > _**Note**:_ MetaDefender API doesn't support chunk upload, however is recommended to stream the files to MetaDefender as part of the upload process.  --- ## File Analysis Process    MetaDefender's main functionality is to analyze large volumes with a high throughput. Depending on the configuration and licensed technologies, the analysis times can vary.    Below is a brief description of the API integration flow:    1. Upload a file for analysis (`POST /file`), which returns the `data_id`: [File Analysis](#operation/fileAnalysisPost)).           > _**Note**:_ The performance depends on:           > - number of nodes (scaling)     > - number of engines per node     > - type of file to be scanned     > - Metadefender Core and nodes' hardware       2. You have 2 ways to retrieve the analysis report:      - **Polling**: Fetch the result with previously received data_id (`GET /file/{data_id}` resource) until scan result belonging to data_id doesn't reach the 100 percent progress_percentage: ( [Fetch processing result](#operation/userLogin))        > _**Note**:_ Too many data_id requests can reduce performance. It is enough to just check every few hundred milliseconds.          - **Callbackurl**: Specify a callbackurl that will be called once the analysis is complete.     3. Retrieve the analysis results anytime after the analysis is completed with hash for files (md5, sha1, sha256) by calling [Fetch processing result](#operation/userLogin).      - The hash can be found in the scan results    4. Retrieve processed file (sanitized, redacted, watermarked, etc.) after the analysis is complete.      > _**Note**:_ Based on the configured retention policy, the files might be available for retrieval at a later time.   --- OPSWAT provides some sample codes on [GitHub](https://github.com/OPSWAT) to make it easier to understand how the MetaDefender REST API works. 

The version of the OpenAPI document: v4.18.0
Contact: feedback@opswat.com
Generated by: https://openapi-generator.tech

=end comment

=cut

#
# NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
# Do not edit the class manually.
# Ref: https://openapi-generator.tech
#
package WWW::OpenAPIClient::BatchApi;

require 5.6.0;
use strict;
use warnings;
use utf8; 
use Exporter;
use Carp qw( croak );
use Log::Any qw($log);

use WWW::OpenAPIClient::ApiClient;

use base "Class::Data::Inheritable";

__PACKAGE__->mk_classdata('method_documentation' => {});

sub new {
    my $class = shift;
    my $api_client;

    if ($_[0] && ref $_[0] && ref $_[0] eq 'WWW::OpenAPIClient::ApiClient' ) {
        $api_client = $_[0];
    } else {
        $api_client = WWW::OpenAPIClient::ApiClient->new(@_);
    }

    bless { api_client => $api_client }, $class;

}


#
# batch_cancel
#
# Cancel Batch
# 
# @param string $batch_id The batch identifier used to submit files in the batch and to close the batch. (required)
# @param string $apikey Generated &#x60;session_id&#x60; from [Login](#operation/userLogin) call can be used as an &#x60;apikey&#x60; for API calls that require authentication.                 (optional)
{
    my $params = {
    'batch_id' => {
        data_type => 'string',
        description => 'The batch identifier used to submit files in the batch and to close the batch.',
        required => '1',
    },
    'apikey' => {
        data_type => 'string',
        description => 'Generated &#x60;session_id&#x60; from [Login](#operation/userLogin) call can be used as an &#x60;apikey&#x60; for API calls that require authentication.                ',
        required => '0',
    },
    };
    __PACKAGE__->method_documentation->{ 'batch_cancel' } = { 
        summary => 'Cancel Batch',
        params => $params,
        returns => 'object',
        };
}
# @return object
#
sub batch_cancel {
    my ($self, %args) = @_;

    # verify the required parameter 'batch_id' is set
    unless (exists $args{'batch_id'}) {
      croak("Missing the required parameter 'batch_id' when calling batch_cancel");
    }

    # parse inputs
    my $_resource_path = '/file/{batchId}/cancel';

    my $_method = 'POST';
    my $query_params = {};
    my $header_params = {};
    my $form_params = {};

    # 'Accept' and 'Content-Type' header
    my $_header_accept = $self->{api_client}->select_header_accept('application/json');
    if ($_header_accept) {
        $header_params->{'Accept'} = $_header_accept;
    }
    $header_params->{'Content-Type'} = $self->{api_client}->select_header_content_type();

    # header params
    if ( exists $args{'apikey'}) {
        $header_params->{'apikey'} = $self->{api_client}->to_header_value($args{'apikey'});
    }

    # path params
    if ( exists $args{'batch_id'}) {
        my $_base_variable = "{" . "batchId" . "}";
        my $_base_value = $self->{api_client}->to_path_value($args{'batch_id'});
        $_resource_path =~ s/$_base_variable/$_base_value/g;
    }

    my $_body_data;
    # authentication setting, if any
    my $auth_settings = [qw()];

    # make the API Call
    my $response = $self->{api_client}->call_api($_resource_path, $_method,
                                           $query_params, $form_params,
                                           $header_params, $_body_data, $auth_settings);
    if (!$response) {
        return;
    }
    my $_response_object = $self->{api_client}->deserialize('object', $response);
    return $_response_object;
}

#
# batch_close
#
# Close Batch
# 
# @param string $batch_id The batch identifier used to submit files in the batch and to close the batch. (required)
# @param string $apikey Generated &#x60;session_id&#x60; from [Login](#operation/userLogin) call can be used as an &#x60;apikey&#x60; for API calls that require authentication.                 (optional)
{
    my $params = {
    'batch_id' => {
        data_type => 'string',
        description => 'The batch identifier used to submit files in the batch and to close the batch.',
        required => '1',
    },
    'apikey' => {
        data_type => 'string',
        description => 'Generated &#x60;session_id&#x60; from [Login](#operation/userLogin) call can be used as an &#x60;apikey&#x60; for API calls that require authentication.                ',
        required => '0',
    },
    };
    __PACKAGE__->method_documentation->{ 'batch_close' } = { 
        summary => 'Close Batch',
        params => $params,
        returns => 'BatchResponse',
        };
}
# @return BatchResponse
#
sub batch_close {
    my ($self, %args) = @_;

    # verify the required parameter 'batch_id' is set
    unless (exists $args{'batch_id'}) {
      croak("Missing the required parameter 'batch_id' when calling batch_close");
    }

    # parse inputs
    my $_resource_path = '/file/batch/{batchId}/close';

    my $_method = 'POST';
    my $query_params = {};
    my $header_params = {};
    my $form_params = {};

    # 'Accept' and 'Content-Type' header
    my $_header_accept = $self->{api_client}->select_header_accept('application/json');
    if ($_header_accept) {
        $header_params->{'Accept'} = $_header_accept;
    }
    $header_params->{'Content-Type'} = $self->{api_client}->select_header_content_type();

    # header params
    if ( exists $args{'apikey'}) {
        $header_params->{'apikey'} = $self->{api_client}->to_header_value($args{'apikey'});
    }

    # path params
    if ( exists $args{'batch_id'}) {
        my $_base_variable = "{" . "batchId" . "}";
        my $_base_value = $self->{api_client}->to_path_value($args{'batch_id'});
        $_resource_path =~ s/$_base_variable/$_base_value/g;
    }

    my $_body_data;
    # authentication setting, if any
    my $auth_settings = [qw()];

    # make the API Call
    my $response = $self->{api_client}->call_api($_resource_path, $_method,
                                           $query_params, $form_params,
                                           $header_params, $_body_data, $auth_settings);
    if (!$response) {
        return;
    }
    my $_response_object = $self->{api_client}->deserialize('BatchResponse', $response);
    return $_response_object;
}

#
# batch_create
#
# Initiate Batch
# 
# @param string $apikey Generated &#x60;session_id&#x60; from [Login](#operation/userLogin) call can be used as an &#x60;apikey&#x60; for API calls that require authentication.                 (optional)
# @param string $rule Select rule for the analysis, if no header given the default rule will be selected (URL encoded string of rule name)        (optional)
# @param string $user_agent user_agent header used to identify (and limit) access to a particular rule. For rule selection, &#x60;rule&#x60; header should be used.  (optional)
# @param string $user_data Additional custom information (max 1024 bytes, URL encoded UTF-8 string)        (optional)
{
    my $params = {
    'apikey' => {
        data_type => 'string',
        description => 'Generated &#x60;session_id&#x60; from [Login](#operation/userLogin) call can be used as an &#x60;apikey&#x60; for API calls that require authentication.                ',
        required => '0',
    },
    'rule' => {
        data_type => 'string',
        description => 'Select rule for the analysis, if no header given the default rule will be selected (URL encoded string of rule name)       ',
        required => '0',
    },
    'user_agent' => {
        data_type => 'string',
        description => 'user_agent header used to identify (and limit) access to a particular rule. For rule selection, &#x60;rule&#x60; header should be used. ',
        required => '0',
    },
    'user_data' => {
        data_type => 'string',
        description => 'Additional custom information (max 1024 bytes, URL encoded UTF-8 string)       ',
        required => '0',
    },
    };
    __PACKAGE__->method_documentation->{ 'batch_create' } = { 
        summary => 'Initiate Batch',
        params => $params,
        returns => 'BatchId',
        };
}
# @return BatchId
#
sub batch_create {
    my ($self, %args) = @_;

    # parse inputs
    my $_resource_path = '/file/batch';

    my $_method = 'POST';
    my $query_params = {};
    my $header_params = {};
    my $form_params = {};

    # 'Accept' and 'Content-Type' header
    my $_header_accept = $self->{api_client}->select_header_accept('application/json');
    if ($_header_accept) {
        $header_params->{'Accept'} = $_header_accept;
    }
    $header_params->{'Content-Type'} = $self->{api_client}->select_header_content_type();

    # header params
    if ( exists $args{'apikey'}) {
        $header_params->{'apikey'} = $self->{api_client}->to_header_value($args{'apikey'});
    }

    # header params
    if ( exists $args{'rule'}) {
        $header_params->{'rule'} = $self->{api_client}->to_header_value($args{'rule'});
    }

    # header params
    if ( exists $args{'user_agent'}) {
        $header_params->{'user_agent'} = $self->{api_client}->to_header_value($args{'user_agent'});
    }

    # header params
    if ( exists $args{'user_data'}) {
        $header_params->{'user-data'} = $self->{api_client}->to_header_value($args{'user_data'});
    }

    my $_body_data;
    # authentication setting, if any
    my $auth_settings = [qw()];

    # make the API Call
    my $response = $self->{api_client}->call_api($_resource_path, $_method,
                                           $query_params, $form_params,
                                           $header_params, $_body_data, $auth_settings);
    if (!$response) {
        return;
    }
    my $_response_object = $self->{api_client}->deserialize('BatchId', $response);
    return $_response_object;
}

#
# batch_signed_result
#
# Download Signed Batch Result
# 
# @param string $batch_id The batch identifier used to submit files in the batch and to close the batch. (required)
# @param string $apikey Generated &#x60;session_id&#x60; from [Login](#operation/userLogin) call can be used as an &#x60;apikey&#x60; for API calls that require authentication.                 (optional)
{
    my $params = {
    'batch_id' => {
        data_type => 'string',
        description => 'The batch identifier used to submit files in the batch and to close the batch.',
        required => '1',
    },
    'apikey' => {
        data_type => 'string',
        description => 'Generated &#x60;session_id&#x60; from [Login](#operation/userLogin) call can be used as an &#x60;apikey&#x60; for API calls that require authentication.                ',
        required => '0',
    },
    };
    __PACKAGE__->method_documentation->{ 'batch_signed_result' } = { 
        summary => 'Download Signed Batch Result',
        params => $params,
        returns => undef,
        };
}
# @return void
#
sub batch_signed_result {
    my ($self, %args) = @_;

    # verify the required parameter 'batch_id' is set
    unless (exists $args{'batch_id'}) {
      croak("Missing the required parameter 'batch_id' when calling batch_signed_result");
    }

    # parse inputs
    my $_resource_path = '/file/batch/{batchId}/certificate';

    my $_method = 'GET';
    my $query_params = {};
    my $header_params = {};
    my $form_params = {};

    # 'Accept' and 'Content-Type' header
    my $_header_accept = $self->{api_client}->select_header_accept('text/plain', 'application/json');
    if ($_header_accept) {
        $header_params->{'Accept'} = $_header_accept;
    }
    $header_params->{'Content-Type'} = $self->{api_client}->select_header_content_type();

    # header params
    if ( exists $args{'apikey'}) {
        $header_params->{'apikey'} = $self->{api_client}->to_header_value($args{'apikey'});
    }

    # path params
    if ( exists $args{'batch_id'}) {
        my $_base_variable = "{" . "batchId" . "}";
        my $_base_value = $self->{api_client}->to_path_value($args{'batch_id'});
        $_resource_path =~ s/$_base_variable/$_base_value/g;
    }

    my $_body_data;
    # authentication setting, if any
    my $auth_settings = [qw()];

    # make the API Call
    $self->{api_client}->call_api($_resource_path, $_method,
                                           $query_params, $form_params,
                                           $header_params, $_body_data, $auth_settings);
    return;
}

#
# batch_status
#
# Status of Batch Analysis
# 
# @param string $batch_id The batch identifier used to submit files in the batch and to close the batch. (required)
# @param string $apikey Generated &#x60;session_id&#x60; from [Login](#operation/userLogin) call can be used as an &#x60;apikey&#x60; for API calls that require authentication.                 (optional)
{
    my $params = {
    'batch_id' => {
        data_type => 'string',
        description => 'The batch identifier used to submit files in the batch and to close the batch.',
        required => '1',
    },
    'apikey' => {
        data_type => 'string',
        description => 'Generated &#x60;session_id&#x60; from [Login](#operation/userLogin) call can be used as an &#x60;apikey&#x60; for API calls that require authentication.                ',
        required => '0',
    },
    };
    __PACKAGE__->method_documentation->{ 'batch_status' } = { 
        summary => 'Status of Batch Analysis',
        params => $params,
        returns => 'BatchResponse',
        };
}
# @return BatchResponse
#
sub batch_status {
    my ($self, %args) = @_;

    # verify the required parameter 'batch_id' is set
    unless (exists $args{'batch_id'}) {
      croak("Missing the required parameter 'batch_id' when calling batch_status");
    }

    # parse inputs
    my $_resource_path = '/file/batch/{batchId}';

    my $_method = 'GET';
    my $query_params = {};
    my $header_params = {};
    my $form_params = {};

    # 'Accept' and 'Content-Type' header
    my $_header_accept = $self->{api_client}->select_header_accept('application/json');
    if ($_header_accept) {
        $header_params->{'Accept'} = $_header_accept;
    }
    $header_params->{'Content-Type'} = $self->{api_client}->select_header_content_type();

    # header params
    if ( exists $args{'apikey'}) {
        $header_params->{'apikey'} = $self->{api_client}->to_header_value($args{'apikey'});
    }

    # path params
    if ( exists $args{'batch_id'}) {
        my $_base_variable = "{" . "batchId" . "}";
        my $_base_value = $self->{api_client}->to_path_value($args{'batch_id'});
        $_resource_path =~ s/$_base_variable/$_base_value/g;
    }

    my $_body_data;
    # authentication setting, if any
    my $auth_settings = [qw()];

    # make the API Call
    my $response = $self->{api_client}->call_api($_resource_path, $_method,
                                           $query_params, $form_params,
                                           $header_params, $_body_data, $auth_settings);
    if (!$response) {
        return;
    }
    my $_response_object = $self->{api_client}->deserialize('BatchResponse', $response);
    return $_response_object;
}

1;