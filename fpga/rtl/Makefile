BUILD_DIR ?= build
TOP := retrocore_top

.PHONY: test synth clean

test:
	mkdir -p $(BUILD_DIR)
	iverilog -g2012 -o $(BUILD_DIR)/tb $(TOP).v tb_$(TOP).v
	vvp $(BUILD_DIR)/tb

synth:
	mkdir -p $(BUILD_DIR)
	yosys -p 'synth_ecp5 -top $(TOP) -json $(BUILD_DIR)/$(TOP).json' $(TOP).v

# A physical ECP5UM-45K bitstream target is intentionally deferred until
# the exact Rev A device/package and board constraints are frozen.
clean:
	rm -rf $(BUILD_DIR)
