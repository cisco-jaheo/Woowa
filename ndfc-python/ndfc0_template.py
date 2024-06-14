#!/usr/bin/python
# Author Ahamed Sadayan


easy_fabric = {'asn': '65513',
"templateName": "Easy_Fabric_11_1",
    "nvPairs": {
        "BGP_AS": "65513",
        "UNDERLAY_IS_V6": false,
        "USE_LINK_LOCAL": "",
        "FABRIC_INTERFACE_TYPE": "p2p",
        "SUBNET_TARGET_MASK": "30",
        "V6_SUBNET_TARGET_MASK": "",
        "LINK_STATE_ROUTING": "ospf",
        "RR_COUNT": "2",
        "ANYCAST_GW_MAC": "0000.face.deed",
        "software_image": "",
        "ENABLE_TRM": false,
        "ENABLE_VPC_PEER_LINK_NATIVE_VLAN": false,
        "VPC_ENABLE_IPv6_ND_SYNC": true,
        "ADVERTISE_PIP_BGP": false,
        "ENABLE_FABRIC_VPC_DOMAIN_ID": false,
        "FABRIC_VPC_QOS": false,
        "OSPF_AUTH_ENABLE": false,
        "ISIS_P2P_ENABLE": "",
        "ISIS_AUTH_ENABLE": "",
        "BGP_AUTH_ENABLE": false,
        "PIM_HELLO_AUTH_ENABLE": false,
        "BFD_ENABLE": false,
        "BFD_IBGP_ENABLE": "",
        "BFD_OSPF_ENABLE": "",
        "BFD_ISIS_ENABLE": "",
        "BFD_PIM_ENABLE": "",
        "BFD_AUTH_ENABLE": "",
        "CDP_ENABLE": false,
        "ENABLE_NGOAM": true,
        "ENABLE_TENANT_DHCP": true,
        "ENABLE_NXAPI": true,
        "ENABLE_NXAPI_HTTP": true,
        "ENABLE_PBR": false,
        "STRICT_CC_MODE": false,
        "AAA_REMOTE_IP_ENABLED": false,
        "SNMP_SERVER_HOST_TRAP": true,
        "FEATURE_PTP": false,
        "MPLS_HANDOFF": false,
        "TCAM_ALLOCATION": true,
        "ENABLE_DEFAULT_QUEUING_POLICY": false,
        "ENABLE_MACSEC": false,
        "STATIC_UNDERLAY_IP_ALLOC": false,
        "AUTO_SYMMETRIC_VRF_LITE": "",
        "BOOTSTRAP_ENABLE": false,
        "DHCP_ENABLE": "",
        "ENABLE_AAA": "",
        "enableRealTimeBackup": false,
        "enableScheduledBackup": false,
        "REPLICATION_MODE": "Multicast",
        "MULTICAST_GROUP_SUBNET": "239.1.1.0/25",
        "L3VNI_MCAST_GROUP": "",
        "RP_COUNT": "2",
        "RP_MODE": "asm",
        "RP_LB_ID": "254",
        "PHANTOM_RP_LB_ID1": "",
        "PHANTOM_RP_LB_ID2": "",
        "PHANTOM_RP_LB_ID3": "",
        "PHANTOM_RP_LB_ID4": "",
        "VPC_PEER_LINK_VLAN": "3600",
        "VPC_PEER_KEEP_ALIVE_OPTION": "management",
        "VPC_AUTO_RECOVERY_TIME": "360",
        "VPC_DELAY_RESTORE": "150",
        "VPC_PEER_LINK_PO": "500",
        "FABRIC_VPC_DOMAIN_ID": "",
        "VPC_DOMAIN_ID_RANGE": "1-1000",
        "FABRIC_VPC_QOS_POLICY_NAME": "",
        "BGP_LB_ID": "0",
        "NVE_LB_ID": "1",
        "ANYCAST_LB_ID": "",
        "LINK_STATE_ROUTING_TAG": "UNDERLAY",
        "OSPF_AREA_ID": "0.0.0.0",
        "OSPF_AUTH_KEY_ID": "",
        "OSPF_AUTH_KEY": "",
        "ISIS_LEVEL": "",
        "ISIS_AUTH_KEYCHAIN_NAME": "",
        "ISIS_AUTH_KEYCHAIN_KEY_ID": "",
        "ISIS_AUTH_KEY": "",
        "BGP_AUTH_KEY_TYPE": "",
        "BGP_AUTH_KEY": "",
        "PIM_HELLO_AUTH_KEY": "",
        "BFD_AUTH_KEY_ID": "",
        "BFD_AUTH_KEY": "",
        "IBGP_PEER_TEMPLATE": "",
        "IBGP_PEER_TEMPLATE_LEAF": "",
        "default_vrf": "Default_VRF_Universal",
        "default_network": "Default_Network_Universal",
        "vrf_extension_template": "Default_VRF_Extension_Universal",
        "network_extension_template": "Default_Network_Extension_Universal",
        "SITE_ID": "65002",
        "FABRIC_MTU": "9216",
        "L2_HOST_INTF_MTU": "9216",
        "POWER_REDUNDANCY_MODE": "ps-redundant",
        "COPP_POLICY": "strict",
        "HD_TIME": "180",
        "BROWNFIELD_NETWORK_NAME_FORMAT": "Auto_Net_VNI$$VNI$$_VLAN$$VLAN_ID$$",
        "GRFIELD_DEBUG_FLAG": "Disable",
        "PTP_LB_ID": "",
        "PTP_DOMAIN_ID": "",
        "MPLS_LB_ID": "",
        "DEAFULT_QUEUING_POLICY_CLOUDSCALE": "",
        "DEAFULT_QUEUING_POLICY_R_SERIES": "",
        "DEAFULT_QUEUING_POLICY_OTHER": "",
        "MACSEC_KEY_STRING": "",
        "MACSEC_ALGORITHM": "",
        "MACSEC_FALLBACK_KEY_STRING": "",
        "MACSEC_FALLBACK_ALGORITHM": "",
        "MACSEC_CIPHER_SUITE": "",
        "MACSEC_REPORT_TIMER": "",
        "EXTRA_CONF_LEAF": "",
        "EXTRA_CONF_SPINE": "",
        "EXTRA_CONF_INTRA_LINKS": "",
        "LOOPBACK0_IP_RANGE": "10.2.0.0/22",
        "LOOPBACK1_IP_RANGE": "10.3.0.0/22",
        "ANYCAST_RP_IP_RANGE": "10.254.254.0/24",
        "SUBNET_RANGE": "10.4.0.0/16",
        "MPLS_LOOPBACK_IP_RANGE": "",
        "LOOPBACK0_IPV6_RANGE": "",
        "LOOPBACK1_IPV6_RANGE": "",
        "V6_SUBNET_RANGE": "",
        "ROUTER_ID_RANGE": "",
        "L2_SEGMENT_ID_RANGE": "30000-49000",
        "L3_PARTITION_ID_RANGE": "50000-59000",
        "NETWORK_VLAN_RANGE": "2300-2999",
        "VRF_VLAN_RANGE": "2000-2299",
        "SUBINTERFACE_RANGE": "2-511",
        "VRF_LITE_AUTOCONFIG": "Manual",
        "DCI_SUBNET_RANGE": "10.33.0.0/16",
        "DCI_SUBNET_TARGET_MASK": "30",
        "SERVICE_NETWORK_VLAN_RANGE": "3000-3199",
        "ROUTE_MAP_SEQUENCE_NUMBER_RANGE": "1-65534",
        "DNS_SERVER_IP_LIST": "",
        "DNS_SERVER_VRF": "",
        "NTP_SERVER_IP_LIST": "",
        "NTP_SERVER_VRF": "",
        "SYSLOG_SERVER_IP_LIST": "",
        "SYSLOG_SEV": "",
        "SYSLOG_SERVER_VRF": "",
        "AAA_SERVER_CONF": "",
        "DHCP_IPV6_ENABLE": "",
        "DHCP_START": "",
        "DHCP_END": "",
        "MGMT_GW": "",
        "MGMT_PREFIX": "",
        "MGMT_V6PREFIX": "",
        "BOOTSTRAP_CONF": "",
        "BOOTSTRAP_MULTISUBNET": "",
        "scheduledTime": "",
        "FABRIC_NAME": "test1",
        "ENABLE_FABRIC_VPC_DOMAIN_ID_PREV": "",
        "FABRIC_VPC_DOMAIN_ID_PREV": "",
        "LINK_STATE_ROUTING_TAG_PREV": "",
        "FABRIC_MTU_PREV": "9216",
        "L2_HOST_INTF_MTU_PREV": "9216",
        "DEPLOYMENT_FREEZE": "false",
        "VPC_DELAY_RESTORE_TIME": "60",
        "FABRIC_TYPE": "Switch_Fabric",
        "ENABLE_AGENT": "false",
        "AGENT_INTF": "eth0",
        "SSPINE_ADD_DEL_DEBUG_FLAG": "Disable",
        "BRFIELD_DEBUG_FLAG": "Disable",
        "ACTIVE_MIGRATION": "false",
        "FF": "Easy_Fabric",
        "MSO_SITE_ID": "",
        "MSO_CONTROLER_ID": "",
        "MSO_SITE_GROUP_NAME": "",
        "PREMSO_PARENT_FABRIC": "",
        "MSO_CONNECTIVITY_DEPLOYED": "",
        "ANYCAST_RP_IP_RANGE_INTERNAL": "",
        "DHCP_START_INTERNAL": "",
        "DHCP_END_INTERNAL": "",
        "MGMT_GW_INTERNAL": "",
        "MGMT_PREFIX_INTERNAL": "",
        "BOOTSTRAP_MULTISUBNET_INTERNAL": "",
        "MGMT_V6PREFIX_INTERNAL": "",
        "DHCP_IPV6_ENABLE_INTERNAL": "",
        "ENABLE_EVPN": "true",
        "FEATURE_PTP_INTERNAL": "false",
        "SSPINE_COUNT": "0",
        "SPINE_COUNT": "0",
        "abstract_feature_leaf": "base_feature_leaf_upg",
        "abstract_feature_spine": "base_feature_spine_upg",
        "abstract_dhcp": "base_dhcp",
        "abstract_multicast": "base_multicast_11_1",
        "abstract_anycast_rp": "anycast_rp",
        "abstract_loopback_interface": "int_fabric_loopback_11_1",
        "abstract_isis": "base_isis_level2",
        "abstract_ospf": "base_ospf",
        "abstract_vpc_domain": "base_vpc_domain_11_1",
        "abstract_vlan_interface": "int_fabric_vlan_11_1",
        "abstract_isis_interface": "isis_interface",
        "abstract_ospf_interface": "ospf_interface_11_1",
        "abstract_pim_interface": "pim_interface",
        "abstract_route_map": "route_map",
        "abstract_bgp": "base_bgp",
        "abstract_bgp_rr": "evpn_bgp_rr",
        "abstract_bgp_neighbor": "evpn_bgp_rr_neighbor",
        "abstract_extra_config_leaf": "extra_config_leaf",
        "abstract_extra_config_bootstrap": "extra_config_bootstrap_11_1",
        "abstract_extra_config_spine": "extra_config_spine",
        "temp_anycast_gateway": "anycast_gateway",
        "temp_vpc_domain_mgmt": "vpc_domain_mgmt",
        "temp_vpc_peer_link": "int_vpc_peer_link_po_11_1",
        "abstract_routed_host": "int_routed_host_11_1",
        "abstract_trunk_host": "int_trunk_host_11_1"
    }
}
