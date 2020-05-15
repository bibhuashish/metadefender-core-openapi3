/**
 * MetaDefender Core
 * ## Developer Guide This is the API documentation for *MetaDefender Core Public API*.  If you would like to evaluate or have any questions about this documentation, please contact us via our [Contact Us](https://opswat.com/contact) form.  ## How to Interact with MetaDefender Core using REST Beginning with MetaDefender Core 4.x, OPSWAT recommends using the JSON-based REST API. The available methods are documented below. > _**Note**:_ MetaDefender API doesn't support chunk upload, however is recommended to stream the files to MetaDefender as part of the upload process.  --- ## File Analysis Process    MetaDefender's main functionality is to analyze large volumes with a high throughput. Depending on the configuration and licensed technologies, the analysis times can vary.    Below is a brief description of the API integration flow:    1. Upload a file for analysis (`POST /file`), which returns the `data_id`: [File Analysis](#operation/fileAnalysisPost)).           > _**Note**:_ The performance depends on:           > - number of nodes (scaling)     > - number of engines per node     > - type of file to be scanned     > - Metadefender Core and nodes' hardware       2. You have 2 ways to retrieve the analysis report:      - **Polling**: Fetch the result with previously received data_id (`GET /file/{data_id}` resource) until scan result belonging to data_id doesn't reach the 100 percent progress_percentage: ( [Fetch processing result](#operation/userLogin))        > _**Note**:_ Too many data_id requests can reduce performance. It is enough to just check every few hundred milliseconds.          - **Callbackurl**: Specify a callbackurl that will be called once the analysis is complete.     3. Retrieve the analysis results anytime after the analysis is completed with hash for files (md5, sha1, sha256) by calling [Fetch processing result](#operation/userLogin).      - The hash can be found in the scan results    4. Retrieve processed file (sanitized, redacted, watermarked, etc.) after the analysis is complete.      > _**Note**:_ Based on the configured retention policy, the files might be available for retrieval at a later time.   --- OPSWAT provides some sample codes on [GitHub](https://github.com/OPSWAT) to make it easier to understand how the MetaDefender REST API works. 
 *
 * The version of the OpenAPI document: v4.18.0
 * Contact: feedback@opswat.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAnalysisResult_process_info_post_processing.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAnalysisResult_process_info_post_processing::OAIAnalysisResult_process_info_post_processing(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAnalysisResult_process_info_post_processing::OAIAnalysisResult_process_info_post_processing() {
    this->initializeModel();
}

OAIAnalysisResult_process_info_post_processing::~OAIAnalysisResult_process_info_post_processing() {}

void OAIAnalysisResult_process_info_post_processing::initializeModel() {

    m_actions_failed_isSet = false;
    m_actions_failed_isValid = false;

    m_actions_ran_isSet = false;
    m_actions_ran_isValid = false;

    m_converted_destination_isSet = false;
    m_converted_destination_isValid = false;

    m_converted_to_isSet = false;
    m_converted_to_isValid = false;

    m_copy_move_destination_isSet = false;
    m_copy_move_destination_isValid = false;

    m_sanitization_details_isSet = false;
    m_sanitization_details_isValid = false;
}

void OAIAnalysisResult_process_info_post_processing::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAnalysisResult_process_info_post_processing::fromJsonObject(QJsonObject json) {

    m_actions_failed_isValid = ::OpenAPI::fromJsonValue(actions_failed, json[QString("actions_failed")]);
    m_actions_failed_isSet = !json[QString("actions_failed")].isNull() && m_actions_failed_isValid;

    m_actions_ran_isValid = ::OpenAPI::fromJsonValue(actions_ran, json[QString("actions_ran")]);
    m_actions_ran_isSet = !json[QString("actions_ran")].isNull() && m_actions_ran_isValid;

    m_converted_destination_isValid = ::OpenAPI::fromJsonValue(converted_destination, json[QString("converted_destination")]);
    m_converted_destination_isSet = !json[QString("converted_destination")].isNull() && m_converted_destination_isValid;

    m_converted_to_isValid = ::OpenAPI::fromJsonValue(converted_to, json[QString("converted_to")]);
    m_converted_to_isSet = !json[QString("converted_to")].isNull() && m_converted_to_isValid;

    m_copy_move_destination_isValid = ::OpenAPI::fromJsonValue(copy_move_destination, json[QString("copy_move_destination")]);
    m_copy_move_destination_isSet = !json[QString("copy_move_destination")].isNull() && m_copy_move_destination_isValid;

    m_sanitization_details_isValid = ::OpenAPI::fromJsonValue(sanitization_details, json[QString("sanitization_details")]);
    m_sanitization_details_isSet = !json[QString("sanitization_details")].isNull() && m_sanitization_details_isValid;
}

QString OAIAnalysisResult_process_info_post_processing::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAnalysisResult_process_info_post_processing::asJsonObject() const {
    QJsonObject obj;
    if (m_actions_failed_isSet) {
        obj.insert(QString("actions_failed"), ::OpenAPI::toJsonValue(actions_failed));
    }
    if (m_actions_ran_isSet) {
        obj.insert(QString("actions_ran"), ::OpenAPI::toJsonValue(actions_ran));
    }
    if (m_converted_destination_isSet) {
        obj.insert(QString("converted_destination"), ::OpenAPI::toJsonValue(converted_destination));
    }
    if (m_converted_to_isSet) {
        obj.insert(QString("converted_to"), ::OpenAPI::toJsonValue(converted_to));
    }
    if (m_copy_move_destination_isSet) {
        obj.insert(QString("copy_move_destination"), ::OpenAPI::toJsonValue(copy_move_destination));
    }
    if (sanitization_details.isSet()) {
        obj.insert(QString("sanitization_details"), ::OpenAPI::toJsonValue(sanitization_details));
    }
    return obj;
}

QString OAIAnalysisResult_process_info_post_processing::getActionsFailed() const {
    return actions_failed;
}
void OAIAnalysisResult_process_info_post_processing::setActionsFailed(const QString &actions_failed) {
    this->actions_failed = actions_failed;
    this->m_actions_failed_isSet = true;
}

QString OAIAnalysisResult_process_info_post_processing::getActionsRan() const {
    return actions_ran;
}
void OAIAnalysisResult_process_info_post_processing::setActionsRan(const QString &actions_ran) {
    this->actions_ran = actions_ran;
    this->m_actions_ran_isSet = true;
}

QString OAIAnalysisResult_process_info_post_processing::getConvertedDestination() const {
    return converted_destination;
}
void OAIAnalysisResult_process_info_post_processing::setConvertedDestination(const QString &converted_destination) {
    this->converted_destination = converted_destination;
    this->m_converted_destination_isSet = true;
}

QString OAIAnalysisResult_process_info_post_processing::getConvertedTo() const {
    return converted_to;
}
void OAIAnalysisResult_process_info_post_processing::setConvertedTo(const QString &converted_to) {
    this->converted_to = converted_to;
    this->m_converted_to_isSet = true;
}

QString OAIAnalysisResult_process_info_post_processing::getCopyMoveDestination() const {
    return copy_move_destination;
}
void OAIAnalysisResult_process_info_post_processing::setCopyMoveDestination(const QString &copy_move_destination) {
    this->copy_move_destination = copy_move_destination;
    this->m_copy_move_destination_isSet = true;
}

OAIDeepCDRDetails OAIAnalysisResult_process_info_post_processing::getSanitizationDetails() const {
    return sanitization_details;
}
void OAIAnalysisResult_process_info_post_processing::setSanitizationDetails(const OAIDeepCDRDetails &sanitization_details) {
    this->sanitization_details = sanitization_details;
    this->m_sanitization_details_isSet = true;
}

bool OAIAnalysisResult_process_info_post_processing::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_actions_failed_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_actions_ran_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_converted_destination_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_converted_to_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_copy_move_destination_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (sanitization_details.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAnalysisResult_process_info_post_processing::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI