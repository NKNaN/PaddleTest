# api:paddle.nn.functional.conv._conv_nd||api:paddle.nn.functional.activation.relu||api:paddle.nn.functional.pooling.max_pool2d||api:paddle.nn.functional.conv._conv_nd||api:paddle.nn.functional.activation.relu||api:paddle.nn.functional.conv._conv_nd||api:paddle.nn.functional.activation.relu||api:paddle.nn.functional.conv._conv_nd||api:paddle.nn.functional.activation.relu||api:paddle.tensor.manipulation.concat||api:paddle.nn.functional.conv._conv_nd||api:paddle.nn.functional.activation.relu||api:paddle.nn.functional.conv._conv_nd||api:paddle.nn.functional.activation.relu||api:paddle.nn.functional.conv._conv_nd||api:paddle.nn.functional.activation.relu||api:paddle.tensor.manipulation.concat||api:paddle.nn.functional.conv._conv_nd||api:paddle.nn.functional.activation.relu||api:paddle.nn.functional.conv._conv_nd||api:paddle.nn.functional.activation.relu||api:paddle.nn.functional.conv._conv_nd||api:paddle.nn.functional.activation.relu||api:paddle.tensor.manipulation.concat||api:paddle.nn.functional.pooling.max_pool2d||api:paddle.nn.functional.conv._conv_nd||api:paddle.nn.functional.activation.relu||api:paddle.nn.functional.conv._conv_nd||api:paddle.nn.functional.activation.relu||api:paddle.nn.functional.conv._conv_nd||api:paddle.nn.functional.activation.relu||api:paddle.tensor.manipulation.concat||api:paddle.nn.functional.conv._conv_nd||api:paddle.nn.functional.activation.relu||api:paddle.nn.functional.conv._conv_nd||api:paddle.nn.functional.activation.relu||api:paddle.nn.functional.conv._conv_nd||api:paddle.nn.functional.activation.relu||api:paddle.tensor.manipulation.concat||api:paddle.nn.functional.conv._conv_nd||api:paddle.nn.functional.activation.relu||api:paddle.nn.functional.conv._conv_nd||api:paddle.nn.functional.activation.relu||api:paddle.nn.functional.conv._conv_nd||api:paddle.nn.functional.activation.relu||api:paddle.tensor.manipulation.concat||api:paddle.nn.functional.conv._conv_nd||api:paddle.nn.functional.activation.relu||api:paddle.nn.functional.conv._conv_nd||api:paddle.nn.functional.activation.relu||api:paddle.nn.functional.conv._conv_nd||api:paddle.nn.functional.activation.relu||api:paddle.tensor.manipulation.concat||api:paddle.nn.functional.pooling.max_pool2d||api:paddle.nn.functional.conv._conv_nd||api:paddle.nn.functional.activation.relu||api:paddle.nn.functional.conv._conv_nd||api:paddle.nn.functional.activation.relu||api:paddle.nn.functional.conv._conv_nd||api:paddle.nn.functional.activation.relu||api:paddle.tensor.manipulation.concat||api:paddle.nn.functional.common.dropout||api:paddle.nn.functional.conv._conv_nd||api:paddle.nn.functional.activation.relu||api:paddle.nn.functional.pooling.adaptive_avg_pool2d||api:paddle.tensor.manipulation.squeeze
import paddle
import unittest
import numpy as np


class LayerCase(paddle.nn.Layer):
    def __init__(self):
        super().__init__()
        self.parameter_0 = self.create_parameter(
           shape=[256, 64, 1, 1],
           dtype=paddle.float32,
        )
        self.parameter_1 = self.create_parameter(
           shape=[256],
           dtype=paddle.float32,
        )
        self.parameter_2 = self.create_parameter(
           shape=[96],
           dtype=paddle.float32,
        )
        self.parameter_3 = self.create_parameter(
           shape=[192],
           dtype=paddle.float32,
        )
        self.parameter_4 = self.create_parameter(
           shape=[64, 16, 1, 1],
           dtype=paddle.float32,
        )
        self.parameter_5 = self.create_parameter(
           shape=[128, 32, 1, 1],
           dtype=paddle.float32,
        )
        self.parameter_6 = self.create_parameter(
           shape=[64, 16, 1, 1],
           dtype=paddle.float32,
        )
        self.parameter_7 = self.create_parameter(
           shape=[32],
           dtype=paddle.float32,
        )
        self.parameter_8 = self.create_parameter(
           shape=[192, 48, 3, 3],
           dtype=paddle.float32,
        )
        self.parameter_9 = self.create_parameter(
           shape=[128, 32, 3, 3],
           dtype=paddle.float32,
        )
        self.parameter_10 = self.create_parameter(
           shape=[32, 256, 1, 1],
           dtype=paddle.float32,
        )
        self.parameter_11 = self.create_parameter(
           shape=[64, 16, 3, 3],
           dtype=paddle.float32,
        )
        self.parameter_12 = self.create_parameter(
           shape=[32, 128, 1, 1],
           dtype=paddle.float32,
        )
        self.parameter_13 = self.create_parameter(
           shape=[48],
           dtype=paddle.float32,
        )
        self.parameter_14 = self.create_parameter(
           shape=[128],
           dtype=paddle.float32,
        )
        self.parameter_15 = self.create_parameter(
           shape=[1000, 512, 1, 1],
           dtype=paddle.float32,
        )
        self.parameter_16 = self.create_parameter(
           shape=[128, 32, 1, 1],
           dtype=paddle.float32,
        )
        self.parameter_17 = self.create_parameter(
           shape=[1000],
           dtype=paddle.float32,
        )
        self.parameter_18 = self.create_parameter(
           shape=[256, 64, 1, 1],
           dtype=paddle.float32,
        )
        self.parameter_19 = self.create_parameter(
           shape=[48],
           dtype=paddle.float32,
        )
        self.parameter_20 = self.create_parameter(
           shape=[256],
           dtype=paddle.float32,
        )
        self.parameter_21 = self.create_parameter(
           shape=[192],
           dtype=paddle.float32,
        )
        self.parameter_22 = self.create_parameter(
           shape=[64],
           dtype=paddle.float32,
        )
        self.parameter_23 = self.create_parameter(
           shape=[16],
           dtype=paddle.float32,
        )
        self.parameter_24 = self.create_parameter(
           shape=[16, 128, 1, 1],
           dtype=paddle.float32,
        )
        self.parameter_25 = self.create_parameter(
           shape=[64, 16, 3, 3],
           dtype=paddle.float32,
        )
        self.parameter_26 = self.create_parameter(
           shape=[192],
           dtype=paddle.float32,
        )
        self.parameter_27 = self.create_parameter(
           shape=[64, 384, 1, 1],
           dtype=paddle.float32,
        )
        self.parameter_28 = self.create_parameter(
           shape=[192, 48, 3, 3],
           dtype=paddle.float32,
        )
        self.parameter_29 = self.create_parameter(
           shape=[128, 32, 3, 3],
           dtype=paddle.float32,
        )
        self.parameter_30 = self.create_parameter(
           shape=[64],
           dtype=paddle.float32,
        )
        self.parameter_31 = self.create_parameter(
           shape=[192, 48, 1, 1],
           dtype=paddle.float32,
        )
        self.parameter_32 = self.create_parameter(
           shape=[192],
           dtype=paddle.float32,
        )
        self.parameter_33 = self.create_parameter(
           shape=[48, 384, 1, 1],
           dtype=paddle.float32,
        )
        self.parameter_34 = self.create_parameter(
           shape=[96, 3, 7, 7],
           dtype=paddle.float32,
        )
        self.parameter_35 = self.create_parameter(
           shape=[16, 96, 1, 1],
           dtype=paddle.float32,
        )
        self.parameter_36 = self.create_parameter(
           shape=[64],
           dtype=paddle.float32,
        )
        self.parameter_37 = self.create_parameter(
           shape=[16],
           dtype=paddle.float32,
        )
        self.parameter_38 = self.create_parameter(
           shape=[64],
           dtype=paddle.float32,
        )
        self.parameter_39 = self.create_parameter(
           shape=[256, 64, 3, 3],
           dtype=paddle.float32,
        )
        self.parameter_40 = self.create_parameter(
           shape=[48, 256, 1, 1],
           dtype=paddle.float32,
        )
        self.parameter_41 = self.create_parameter(
           shape=[64],
           dtype=paddle.float32,
        )
        self.parameter_42 = self.create_parameter(
           shape=[192, 48, 1, 1],
           dtype=paddle.float32,
        )
        self.parameter_43 = self.create_parameter(
           shape=[256],
           dtype=paddle.float32,
        )
        self.parameter_44 = self.create_parameter(
           shape=[128],
           dtype=paddle.float32,
        )
        self.parameter_45 = self.create_parameter(
           shape=[64],
           dtype=paddle.float32,
        )
        self.parameter_46 = self.create_parameter(
           shape=[128],
           dtype=paddle.float32,
        )
        self.parameter_47 = self.create_parameter(
           shape=[128],
           dtype=paddle.float32,
        )
        self.parameter_48 = self.create_parameter(
           shape=[32],
           dtype=paddle.float32,
        )
        self.parameter_49 = self.create_parameter(
           shape=[256],
           dtype=paddle.float32,
        )
        self.parameter_50 = self.create_parameter(
           shape=[64, 512, 1, 1],
           dtype=paddle.float32,
        )
        self.parameter_51 = self.create_parameter(
           shape=[256, 64, 3, 3],
           dtype=paddle.float32,
        )
    def forward(
        self,
        var_0,    # (shape: [11, 3, 224, 224], dtype: paddle.float32, stop_gradient: True)
    ):
        paddle.seed(33)
        var_1 = paddle.nn.functional.conv._conv_nd(var_0, self.parameter_34, bias=self.parameter_2, stride=[2, 2], padding=[0, 0], padding_algorithm='EXPLICIT', dilation=[1, 1], groups=1, data_format='NCHW', channel_dim=1, op_type='conv2d', use_cudnn=True)
        var_2 = paddle.nn.functional.activation.relu(var_1)
        var_3 = paddle.nn.functional.pooling.max_pool2d(var_2, kernel_size=3, stride=2, padding=0, return_mask=False, ceil_mode=False, data_format='NCHW', name=None)
        var_4 = paddle.nn.functional.conv._conv_nd(var_3, self.parameter_35, bias=self.parameter_23, stride=[1, 1], padding=[0, 0], padding_algorithm='EXPLICIT', dilation=[1, 1], groups=1, data_format='NCHW', channel_dim=1, op_type='conv2d', use_cudnn=True)
        var_5 = paddle.nn.functional.activation.relu(var_4)
        var_6 = paddle.nn.functional.conv._conv_nd(var_5, self.parameter_6, bias=self.parameter_45, stride=[1, 1], padding=[0, 0], padding_algorithm='EXPLICIT', dilation=[1, 1], groups=1, data_format='NCHW', channel_dim=1, op_type='conv2d', use_cudnn=True)
        var_7 = paddle.nn.functional.activation.relu(var_6)
        var_8 = paddle.nn.functional.conv._conv_nd(var_5, self.parameter_11, bias=self.parameter_36, stride=[1, 1], padding=[1, 1], padding_algorithm='EXPLICIT', dilation=[1, 1], groups=1, data_format='NCHW', channel_dim=1, op_type='conv2d', use_cudnn=True)
        var_9 = paddle.nn.functional.activation.relu(var_8)
        var_10 = paddle.tensor.manipulation.concat([var_7, var_9], axis=1)
        var_11 = paddle.nn.functional.conv._conv_nd(var_10, self.parameter_24, bias=self.parameter_37, stride=[1, 1], padding=[0, 0], padding_algorithm='EXPLICIT', dilation=[1, 1], groups=1, data_format='NCHW', channel_dim=1, op_type='conv2d', use_cudnn=True)
        var_12 = paddle.nn.functional.activation.relu(var_11)
        var_13 = paddle.nn.functional.conv._conv_nd(var_12, self.parameter_4, bias=self.parameter_30, stride=[1, 1], padding=[0, 0], padding_algorithm='EXPLICIT', dilation=[1, 1], groups=1, data_format='NCHW', channel_dim=1, op_type='conv2d', use_cudnn=True)
        var_14 = paddle.nn.functional.activation.relu(var_13)
        var_15 = paddle.nn.functional.conv._conv_nd(var_12, self.parameter_25, bias=self.parameter_38, stride=[1, 1], padding=[1, 1], padding_algorithm='EXPLICIT', dilation=[1, 1], groups=1, data_format='NCHW', channel_dim=1, op_type='conv2d', use_cudnn=True)
        var_16 = paddle.nn.functional.activation.relu(var_15)
        var_17 = paddle.tensor.manipulation.concat([var_14, var_16], axis=1)
        var_18 = paddle.nn.functional.conv._conv_nd(var_17, self.parameter_12, bias=self.parameter_7, stride=[1, 1], padding=[0, 0], padding_algorithm='EXPLICIT', dilation=[1, 1], groups=1, data_format='NCHW', channel_dim=1, op_type='conv2d', use_cudnn=True)
        var_19 = paddle.nn.functional.activation.relu(var_18)
        var_20 = paddle.nn.functional.conv._conv_nd(var_19, self.parameter_16, bias=self.parameter_14, stride=[1, 1], padding=[0, 0], padding_algorithm='EXPLICIT', dilation=[1, 1], groups=1, data_format='NCHW', channel_dim=1, op_type='conv2d', use_cudnn=True)
        var_21 = paddle.nn.functional.activation.relu(var_20)
        var_22 = paddle.nn.functional.conv._conv_nd(var_19, self.parameter_9, bias=self.parameter_47, stride=[1, 1], padding=[1, 1], padding_algorithm='EXPLICIT', dilation=[1, 1], groups=1, data_format='NCHW', channel_dim=1, op_type='conv2d', use_cudnn=True)
        var_23 = paddle.nn.functional.activation.relu(var_22)
        var_24 = paddle.tensor.manipulation.concat([var_21, var_23], axis=1)
        var_25 = paddle.nn.functional.pooling.max_pool2d(var_24, kernel_size=3, stride=2, padding=0, return_mask=False, ceil_mode=False, data_format='NCHW', name=None)
        var_26 = paddle.nn.functional.conv._conv_nd(var_25, self.parameter_10, bias=self.parameter_48, stride=[1, 1], padding=[0, 0], padding_algorithm='EXPLICIT', dilation=[1, 1], groups=1, data_format='NCHW', channel_dim=1, op_type='conv2d', use_cudnn=True)
        var_27 = paddle.nn.functional.activation.relu(var_26)
        var_28 = paddle.nn.functional.conv._conv_nd(var_27, self.parameter_5, bias=self.parameter_44, stride=[1, 1], padding=[0, 0], padding_algorithm='EXPLICIT', dilation=[1, 1], groups=1, data_format='NCHW', channel_dim=1, op_type='conv2d', use_cudnn=True)
        var_29 = paddle.nn.functional.activation.relu(var_28)
        var_30 = paddle.nn.functional.conv._conv_nd(var_27, self.parameter_29, bias=self.parameter_46, stride=[1, 1], padding=[1, 1], padding_algorithm='EXPLICIT', dilation=[1, 1], groups=1, data_format='NCHW', channel_dim=1, op_type='conv2d', use_cudnn=True)
        var_31 = paddle.nn.functional.activation.relu(var_30)
        var_32 = paddle.tensor.manipulation.concat([var_29, var_31], axis=1)
        var_33 = paddle.nn.functional.conv._conv_nd(var_32, self.parameter_40, bias=self.parameter_19, stride=[1, 1], padding=[0, 0], padding_algorithm='EXPLICIT', dilation=[1, 1], groups=1, data_format='NCHW', channel_dim=1, op_type='conv2d', use_cudnn=True)
        var_34 = paddle.nn.functional.activation.relu(var_33)
        var_35 = paddle.nn.functional.conv._conv_nd(var_34, self.parameter_42, bias=self.parameter_3, stride=[1, 1], padding=[0, 0], padding_algorithm='EXPLICIT', dilation=[1, 1], groups=1, data_format='NCHW', channel_dim=1, op_type='conv2d', use_cudnn=True)
        var_36 = paddle.nn.functional.activation.relu(var_35)
        var_37 = paddle.nn.functional.conv._conv_nd(var_34, self.parameter_8, bias=self.parameter_32, stride=[1, 1], padding=[1, 1], padding_algorithm='EXPLICIT', dilation=[1, 1], groups=1, data_format='NCHW', channel_dim=1, op_type='conv2d', use_cudnn=True)
        var_38 = paddle.nn.functional.activation.relu(var_37)
        var_39 = paddle.tensor.manipulation.concat([var_36, var_38], axis=1)
        var_40 = paddle.nn.functional.conv._conv_nd(var_39, self.parameter_33, bias=self.parameter_13, stride=[1, 1], padding=[0, 0], padding_algorithm='EXPLICIT', dilation=[1, 1], groups=1, data_format='NCHW', channel_dim=1, op_type='conv2d', use_cudnn=True)
        var_41 = paddle.nn.functional.activation.relu(var_40)
        var_42 = paddle.nn.functional.conv._conv_nd(var_41, self.parameter_31, bias=self.parameter_26, stride=[1, 1], padding=[0, 0], padding_algorithm='EXPLICIT', dilation=[1, 1], groups=1, data_format='NCHW', channel_dim=1, op_type='conv2d', use_cudnn=True)
        var_43 = paddle.nn.functional.activation.relu(var_42)
        var_44 = paddle.nn.functional.conv._conv_nd(var_41, self.parameter_28, bias=self.parameter_21, stride=[1, 1], padding=[1, 1], padding_algorithm='EXPLICIT', dilation=[1, 1], groups=1, data_format='NCHW', channel_dim=1, op_type='conv2d', use_cudnn=True)
        var_45 = paddle.nn.functional.activation.relu(var_44)
        var_46 = paddle.tensor.manipulation.concat([var_43, var_45], axis=1)
        var_47 = paddle.nn.functional.conv._conv_nd(var_46, self.parameter_27, bias=self.parameter_22, stride=[1, 1], padding=[0, 0], padding_algorithm='EXPLICIT', dilation=[1, 1], groups=1, data_format='NCHW', channel_dim=1, op_type='conv2d', use_cudnn=True)
        var_48 = paddle.nn.functional.activation.relu(var_47)
        var_49 = paddle.nn.functional.conv._conv_nd(var_48, self.parameter_18, bias=self.parameter_20, stride=[1, 1], padding=[0, 0], padding_algorithm='EXPLICIT', dilation=[1, 1], groups=1, data_format='NCHW', channel_dim=1, op_type='conv2d', use_cudnn=True)
        var_50 = paddle.nn.functional.activation.relu(var_49)
        var_51 = paddle.nn.functional.conv._conv_nd(var_48, self.parameter_51, bias=self.parameter_49, stride=[1, 1], padding=[1, 1], padding_algorithm='EXPLICIT', dilation=[1, 1], groups=1, data_format='NCHW', channel_dim=1, op_type='conv2d', use_cudnn=True)
        var_52 = paddle.nn.functional.activation.relu(var_51)
        var_53 = paddle.tensor.manipulation.concat([var_50, var_52], axis=1)
        var_54 = paddle.nn.functional.pooling.max_pool2d(var_53, kernel_size=3, stride=2, padding=0, return_mask=False, ceil_mode=False, data_format='NCHW', name=None)
        var_55 = paddle.nn.functional.conv._conv_nd(var_54, self.parameter_50, bias=self.parameter_41, stride=[1, 1], padding=[0, 0], padding_algorithm='EXPLICIT', dilation=[1, 1], groups=1, data_format='NCHW', channel_dim=1, op_type='conv2d', use_cudnn=True)
        var_56 = paddle.nn.functional.activation.relu(var_55)
        var_57 = paddle.nn.functional.conv._conv_nd(var_56, self.parameter_0, bias=self.parameter_43, stride=[1, 1], padding=[0, 0], padding_algorithm='EXPLICIT', dilation=[1, 1], groups=1, data_format='NCHW', channel_dim=1, op_type='conv2d', use_cudnn=True)
        var_58 = paddle.nn.functional.activation.relu(var_57)
        var_59 = paddle.nn.functional.conv._conv_nd(var_56, self.parameter_39, bias=self.parameter_1, stride=[1, 1], padding=[1, 1], padding_algorithm='EXPLICIT', dilation=[1, 1], groups=1, data_format='NCHW', channel_dim=1, op_type='conv2d', use_cudnn=True)
        var_60 = paddle.nn.functional.activation.relu(var_59)
        var_61 = paddle.tensor.manipulation.concat([var_58, var_60], axis=1)
        var_62 = paddle.nn.functional.common.dropout(var_61, p=0.5, axis=None, training=self.training, mode='downscale_in_infer', name=None)
        var_63 = paddle.nn.functional.conv._conv_nd(var_62, self.parameter_15, bias=self.parameter_17, stride=[1, 1], padding=[0, 0], padding_algorithm='EXPLICIT', dilation=[1, 1], groups=1, data_format='NCHW', channel_dim=1, op_type='conv2d', use_cudnn=True)
        var_64 = paddle.nn.functional.activation.relu(var_63)
        var_65 = paddle.nn.functional.pooling.adaptive_avg_pool2d(var_64, output_size=1, data_format='NCHW', name=None)
        var_66 = paddle.tensor.manipulation.squeeze(var_65, axis=[2, 3])
        return var_66



def create_inputspec(): 
    inputspec = ( 
        paddle.static.InputSpec(shape=(-1, 3, -1, -1), dtype=paddle.float32, stop_gradient=False), 
    )
    return inputspec

def create_tensor_inputs():
    inputs = (
        paddle.rand(shape=[11, 3, 224, 224], dtype=paddle.float32),
    )
    return inputs


def create_numpy_inputs():
    inputs = (
        np.random.random(size=[11, 3, 224, 224]).astype('float32'),
    )
    return inputs


class TestLayer(unittest.TestCase):
    def setUp(self):
        self.inputs = create_tensor_inputs()
        self.net = LayerCase()
    def train(self, net, to_static, with_prim=False, with_cinn=False):
        if to_static:
            paddle.set_flags({'FLAGS_prim_all': with_prim})
            if with_cinn:
                build_strategy = paddle.static.BuildStrategy()
                build_strategy.build_cinn_pass = True
                net = paddle.jit.to_static(net, build_strategy=build_strategy, full_graph=True)
            else:
                net = paddle.jit.to_static(net, full_graph=True)
        paddle.seed(33)
        outs = net(*self.inputs)
        return outs
    def test_ast_prim_cinn(self):
        st_out = self.train(self.net, to_static=True)
        cinn_out = self.train(self.net, to_static=True, with_prim=True, with_cinn=True)
        for st, cinn in zip(paddle.utils.flatten(st_out), paddle.utils.flatten(cinn_out)):
            np.testing.assert_allclose(st.numpy(), cinn.numpy(), atol=1e-8)


if __name__ == '__main__':
    unittest.main()